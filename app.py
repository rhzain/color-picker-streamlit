"""
Muhammad Raihan Rizky Zain | 140810230049
Praktikum Artificial Intelligence - Color Picker Using K-Means Clustering
"""

import streamlit as st
import numpy as np
import cv2
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def extract_dominant_colors(image, max_k=5):
    # Mengubah gambar dari BGR ke RGB
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Meratakan array gambar menjadi daftar piksel
    pixels = img_rgb.reshape((-1, 3))

    # Hitung jumlah warna unik
    unique_colors = np.unique(pixels, axis=0)
    k = min(max_k, len(unique_colors))

    # Menerapkan K-Means clustering
    kmeans = KMeans(n_clusters=k, random_state=42, n_init='auto')
    kmeans.fit(pixels)

    # Mendapatkan pusat cluster (warna dominan)
    dominant_colors = kmeans.cluster_centers_.astype(int)

    return dominant_colors, kmeans, pixels

def rgb_to_hex(rgb):
    """Mengkonversi RGB ke hex code"""
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

def create_color_palette_html(colors):
    """
    Membuat palet warna menggunakan HTML/CSS dengan hex code.
    """
    html = """
    <style>
    .color-palette {
        display: flex;
        justify-content: center;
        gap: 15px;
        margin: 20px 0;
        flex-wrap: wrap;
    }
    .color-box {
        width: 120px;
        height: 80px;
        border: 2px solid #333;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        transition: transform 0.2s ease;
    }
    .hex-code {
        font-family: 'Courier New', monospace;
        font-weight: bold;
        font-size: 12px;
        user-select: all;
        cursor: text;
        padding: 4px 6px;
        border-radius: 4px;
        background-color: rgba(255,255,255,0.15);
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }
    .color-box:hover {
        transform: scale(1.05);
    }
    </style>
    <div class="color-palette">"""
    
    for color in colors:
        hex_code = rgb_to_hex(color)
        # Menentukan warna teks berdasarkan brightness
        brightness = np.mean(color)
        text_color = 'white' if brightness < 128 else 'black'
        
        html += f"""
        <div class="color-box" style="background-color: {hex_code};">
            <span class="hex-code" style="color: {text_color};">{hex_code}</span>
        </div>"""
    
    html += """
    </div>"""
    return html

def visualize_kmeans_clustering(pixels, kmeans, dominant_colors):
    """
    Membuat visualisasi K-means clustering menggunakan PCA untuk reduksi dimensi.
    """
    # Sampling pixels untuk visualisasi (untuk performa yang lebih baik)
    n_samples = min(5000, len(pixels))
    indices = np.random.choice(len(pixels), n_samples, replace=False)
    sampled_pixels = pixels[indices]
    
    # Prediksi cluster untuk sampled pixels
    labels = kmeans.predict(sampled_pixels)
    
    # Reduksi dimensi dengan PCA (RGB 3D -> 2D)
    pca = PCA(n_components=2)
    pixels_2d = pca.fit_transform(sampled_pixels)
    centers_2d = pca.transform(dominant_colors)
    
    # Membuat plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Plot 1: Scatter plot dengan warna asli
    for i in range(len(dominant_colors)):
        cluster_points = pixels_2d[labels == i]
        if len(cluster_points) > 0:
            ax1.scatter(cluster_points[:, 0], cluster_points[:, 1], 
                       c=sampled_pixels[labels == i]/255.0, s=1, alpha=0.6)
    
    # Menambahkan centroid
    ax1.scatter(centers_2d[:, 0], centers_2d[:, 1], 
               c=dominant_colors/255.0, s=200, marker='x', 
               linewidths=3, edgecolors='black')
    
    ax1.set_title('K-Means Clustering Visualization\n(dengan Warna Asli)')
    ax1.set_xlabel('PCA Component 1')
    ax1.set_ylabel('PCA Component 2')
    
    # Plot 2: Scatter plot dengan warna cluster
    colors_normalized = dominant_colors / 255.0
    for i in range(len(dominant_colors)):
        cluster_points = pixels_2d[labels == i]
        if len(cluster_points) > 0:
            ax2.scatter(cluster_points[:, 0], cluster_points[:, 1], 
                       c=[colors_normalized[i]], s=1, alpha=0.6, 
                       label=f'Cluster {i+1}: {rgb_to_hex(dominant_colors[i])}')
    
    # Menambahkan centroid
    ax2.scatter(centers_2d[:, 0], centers_2d[:, 1], 
               c=colors_normalized, s=200, marker='x', 
               linewidths=3, edgecolors='black')
    
    ax2.set_title('K-Means Clustering Visualization\n(dengan Warna Cluster)')
    ax2.set_xlabel('PCA Component 1')
    ax2.set_ylabel('PCA Component 2')
    ax2.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    
    plt.tight_layout()
    return fig

# --- Antarmuka Streamlit ---
st.set_page_config(page_title="Image Color Picker", layout="wide")
st.title("🎨 Ekstraksi Warna Dominan dari Gambar")
st.write("Unggah gambar untuk melihat warna-warna dominannya.")

uploaded_file = st.file_uploader("Pilih sebuah gambar...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Membaca gambar yang diunggah
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1) # 1 untuk membaca gambar berwarna (BGR)

    st.subheader("🖼️ Gambar Asli")
    st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), caption="Gambar yang Diunggah", use_container_width=True)

    # Menghitung jumlah warna unik dalam gambar
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pixels = img_rgb.reshape((-1, 3))
    unique_colors_count = len(np.unique(pixels, axis=0))
    max_colors = min(5, unique_colors_count)
    
    # Menampilkan informasi tentang warna unik
    st.info(f"Gambar ini memiliki {unique_colors_count} warna unik. Warna dominan yang akan diekstrak: {max_colors}")

    # Langsung mengekstrak warna dominan tanpa tombol
    with st.spinner("Sedang memproses..."):
        # Mengekstrak warna dominan
        dominant_colors, kmeans, pixels = extract_dominant_colors(image, max_k=5)

        st.subheader(f"Palet {len(dominant_colors)} Warna Dominan")
        
        # Menampilkan palet warna dengan HTML yang diperbaiki
        color_palette_html = create_color_palette_html(dominant_colors)
        st.components.v1.html(color_palette_html, height=150)
        
        st.write("Berikut adalah visualisasi bagaimana algoritma K-Means mengelompokkan warna-warna dalam gambar:")
        
        with st.spinner("Membuat visualisasi clustering..."):
            clustering_fig = visualize_kmeans_clustering(pixels, kmeans, dominant_colors)
            st.pyplot(clustering_fig)
        
        st.write("""
        **Penjelasan Visualisasi:**
        - **Plot Kiri**: Menampilkan titik-titik piksel dengan warna aslinya setelah direduksi dimensi dengan PCA
        - **Plot Kanan**: Menampilkan hasil clustering dengan setiap cluster diberi warna yang sama
        - **Tanda X**: Menunjukkan centroid (pusat) dari setiap cluster yang menjadi warna dominan
        - **PCA**: Digunakan untuk mereduksi dimensi RGB (3D) menjadi 2D agar dapat divisualisasikan
        """)
            
else:
    st.info("Silakan unggah file gambar untuk memulai.")

st.sidebar.header("Tentang")
st.sidebar.info(
    "Aplikasi ini menggunakan K-Means clustering untuk mengekstrak "
    "warna-warna dominan dari sebuah gambar. Jumlah warna yang diekstrak "
    "akan disesuaikan dengan jumlah warna unik dalam gambar (maksimal 5). "
    "Dibuat dengan Streamlit."
)

st.sidebar.header("Cara Kerja")
st.sidebar.info(
    "1. **Preprocessing**: Gambar dikonversi dari BGR ke RGB\n"
    "2. **Pixel Extraction**: Setiap pixel diambil nilai RGB-nya\n"
    "3. **K-Means Clustering**: Algoritma mengelompokkan warna yang mirip\n"
    "4. **Centroid**: Pusat cluster menjadi warna dominan\n"
    "5. **Visualization**: PCA mereduksi dimensi untuk visualisasi 2D"
)

st.markdown("---", unsafe_allow_html=True)
st.markdown(
    """
    <div style='text-align: center; color: #888; font-size: 14px; padding: 10px 0 0 0;'>
        Muhammad Raihan Rizky Zain | <b>140810230049</b><br>
    </div>
    """,
    unsafe_allow_html=True
)