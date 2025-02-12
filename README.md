# 🛸 Drone Blog - Flask Web App  

A simple **Flask-based blog** that fetches and displays drone-related blog posts dynamically from an external API.  

## 🚀 Features  
- Fetches blog posts from an external API.  
- Displays posts with **titles, subtitles, images, and content**.  
- Uses **Flask** for backend and **Bootstrap** for styling.  
- Dynamic routing for each blog post.  

---

## 📌 Installation & Setup  

### 1️⃣ Clone the Repository  
```sh
git clone https://github.com/your-username/drone-blog.git
cd drone-blog
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)  
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies  
```sh
pip install -r requirements.txt
```

### 4️⃣ Run the Flask App  
```sh
python app.py
```
Now, open your browser and go to **`http://127.0.0.1:5000/`** to view the blog. 🚀  

---

## 🛠 Project Structure  
```
/drone-blog
│── /static/            # CSS, JS, and assets
│── /templates/         # HTML templates (index.html, post.html)
│── app.py              # Main Flask application
│── requirements.txt    # Python dependencies
│── README.md           # Project Documentation
```

---
 ### Home Page
![image_alt](https://github.com/dbmurali/my_blog_/blob/5be459eaa6cab44384c601c2d4b396bbf70f8999/home_page.png)

### Posts 
![image_alt](https://github.com/dbmurali/my_blog_/blob/5be459eaa6cab44384c601c2d4b396bbf70f8999/posts.png)

### post content
![image_alt](https://github.com/dbmurali/my_blog_/blob/5be459eaa6cab44384c601c2d4b396bbf70f8999/post.png)

### Footer
![immage_alt](https://github.com/dbmurali/my_blog_/blob/5be459eaa6cab44384c601c2d4b396bbf70f8999/footer.png)

## 📝 API Used  
The blog fetches posts from the following API:  
🔗 **https://api.npoint.io/d4656264c8ac08d072a5**  

You can update this API URL with your own data source.

---

