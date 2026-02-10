# Barcode Entry in Reception (Entrada Rápida de Código de Barras)

![Odoo Version](https://img.shields.io/badge/Odoo-19.0-purple?style=flat-square&logo=odoo)
![License](https://img.shields.io/badge/license-LGPL--3-blue?style=flat-square)
![Status](https://img.shields.io/badge/status-Stable-green?style=flat-square)

Optimiza tu flujo de trabajo en almacén permitiendo asignar códigos de barras a los productos directamente desde el albarán de recepción (Picking), sin necesidad de navegar a la ficha del producto.

## 🚀 Características Principales

- **Edición Directa**: Añade un campo editable de "Código de Barras" en la línea de operaciones del albarán.
- **Sincronización Automática**: Al escanear o escribir un código en el albarán, se actualiza automáticamente el campo `barcode` en el maestro del producto.
- **Ahorro de Tiempo**: Elimina los clics innecesarios y las interrupciones en el proceso de recepción de mercancía.
- **Compatible con Lectores**: Diseñado para funcionar perfectamente con lectores de códigos de barras USB/Bluetooth.

## 🛠️ Instalación

1. Clona este repositorio en tu carpeta de `custom_addons`:
   ```bash
   git clone https://github.com/Yis1000/BarCodeCustom.git
   ```
2. Reinicia el servicio de Odoo.
3. Activa el modo desarrollador.
4. Ve a **Aplicaciones**, actualiza la lista de aplicaciones y busca "Barcode Entry in Reception".
5. Haz clic en **Instalar**.

## 📖 Cómo Usar

1. Ve a **Inventario** > **Operaciones** > **Transferencias** (o Recepciones).
2. Crea o abre una recepción existente.
3. En la pestaña **Operaciones**, verás una nueva columna llamada **"Código de Barras"** (o *Barcode*).
4. **Escanea** el producto con tu pistola de códigos o escribe el número manualmente.
5. ¡Listo! El código ya está asignado a ese producto permanentemente.


## 📋 Requisitos

- Odoo 19.0 Community o Enterprise.
- Módulo base `stock` instalado.

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor, abre un "issue" primero para discutir lo que te gustaría cambiar.

1. Haz un Fork del proyecto.
2. Crea tu rama de características (`git checkout -b feature/AmazingFeature`).
3. Haz Commit de tus cambios (`git commit -m 'Add some AmazingFeature'`).
4. Haz Push a la rama (`git push origin feature/AmazingFeature`).
5. Abre un Pull Request.

## 📄 Licencia

Distribuido bajo la licencia LGPL-3. Ver `LICENSE` para más información.

---
**Desarrollado por Yisus**
