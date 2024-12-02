import streamlit as st
import matplotlib.pyplot as plt
import io

def calculate_panels(height, panel_height):
    return -(-height // panel_height)  # Округление вверх

def generate_door_image(width, height, panel_height, panel_count):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.set_aspect('equal')

    # Рисуем панели
    for i in range(panel_count):
        y = i * panel_height
        ax.add_patch(plt.Rectangle((0, y), width, panel_height, edgecolor='black', facecolor='lightgray'))

    ax.set_title(f"Схема ворот: {panel_count} панели")
    ax.set_xlabel("Ширина (мм)")
    ax.set_ylabel("Высота (мм)")

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return buf

st.title("Расчёт секционных ворот")

# Ввод данных
width = st.number_input("Введите ширину ворот (мм):", min_value=1000, max_value=6000, value=3000)
height = st.number_input("Введите высоту ворот (мм):", min_value=1000, max_value=6000, value=2500)
panel_height = st.number_input("Введите высоту одной панели (мм):", min_value=300, max_value=1000, value=500)

if st.button("Рассчитать"):
    # Расчёт
    panel_count = calculate_panels(height, panel_height)
    total_weight = panel_count * 15  # Вес панели 15 кг (пример)
    total_springs = 2  # Для простых ворот всегда 2 пружины

    # Вывод результатов
    st.subheader("Результаты расчёта")
    st.write(f"Количество панелей: {panel_count}")
    st.write(f"Вес ворот: {total_weight} кг")
    st.write(f"Количество пружин: {total_springs}")

    # Генерация изображения
    img_buf = generate_door_image(width, height, panel_height, panel_count)
    st.image(img_buf, caption="Схема ворот", use_column_width=True)
