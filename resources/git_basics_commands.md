# ⚙️ Comandos básicos de Git y GitHub  

> 📘 Esta guía resume los comandos más útiles que necesitarás durante el taller  
> y en tus futuros proyectos. Ideal para repasar o tener abierta mientras trabajas.

---

## 🧩 1. Configuración inicial  

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tuemail@example.com"
````

Verifica:

```bash
git config --list
```

---

## 📁 2. Clonar un repositorio existente

```bash
git clone https://github.com/usuario/nombre-repositorio.git
```

Ejemplo para el taller:

```bash
git clone https://github.com/jona866/merida-tech-week-copilot-workshop.git
```

---

## ✏️ 3. Guardar cambios en tu proyecto

1️⃣ Ver qué cambió:

```bash
git status
```

2️⃣ Agregar los archivos modificados:

```bash
git add .
```

3️⃣ Guardar (commit) con un mensaje:

```bash
git commit -m "Mensaje claro de lo que hiciste"
```

4️⃣ Subir tus cambios a GitHub:

```bash
git push origin main
```

---

## 🔄 4. Actualizar tu repositorio local

Si alguien más hizo cambios en el mismo repo:

```bash
git pull origin main
```

---

## 🧱 5. Crear y cambiar de rama (opcional)

Crear una nueva rama:

```bash
git branch nombre-de-rama
```

Moverte a esa rama:

```bash
git checkout nombre-de-rama
```

Combinarla con la principal:

```bash
git merge nombre-de-rama
```

---

## 🚀 6. Publicar un sitio en GitHub Pages

1️⃣ Sube tu proyecto (HTML/CSS/JS) al repositorio.
2️⃣ En GitHub → **Settings → Pages**.
3️⃣ En *Source*, selecciona:

```
Branch: main
Folder: /(root)
```

4️⃣ Guarda, y obtendrás una URL tipo:

```
https://TU_USUARIO.github.io/nombre-repositorio/
```

---

## 🧩 7. Comandos útiles extra

| Comando                      | Descripción                                |
| ---------------------------- | ------------------------------------------ |
| `git log --oneline`          | Ver historial de commits resumido          |
| `git diff`                   | Ver diferencias entre archivos modificados |
| `git rm nombre-archivo`      | Eliminar un archivo del repositorio        |
| `git restore nombre-archivo` | Revertir cambios antes de hacer commit     |
| `git reset --hard HEAD`      | Restaurar el estado anterior completo      |

---

## 💡 Tips para el taller

* Realiza **commits pequeños y descriptivos**.
* Usa GitHub Desktop si prefieres interfaz gráfica.
* Antes de publicar tu portafolio, asegúrate de tener `index.html` en la raíz del repositorio.
* Usa `git pull` antes de cada clase o sesión para tener la última versión.

