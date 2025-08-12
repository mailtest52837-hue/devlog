from flask import Blueprint, jsonify, request

from db import SessionLocal, Base
from models import Post

routes = Blueprint("routes", __name__)

@routes.route("/posts", methods = ["GET"])
def get_users():
    db = SessionLocal()
    posts = db.query(Post).all()
    result = [{"id": u.id, "title": u.title, "text": u.text, "data": u.created_at} for u in posts]
    db.close()
    return jsonify(result)

@routes.route("/posts", methods = ["POST"])
def save_user():
    data = request.get_json()
    title = data.get("title")
    text = data.get("text")
    db = SessionLocal()
    post = Post(title = title, text = text)
    db.add(post)
    db.commit()
    db.refresh(post)
    db.close()
    return jsonify({"message": f"Пост с заголовком: {title} добавлен. ID: {post.id}"}), 200

@routes.route("/posts/<int:post_id>", methods = ["PUT"])
def put_user(post_id):
    db = SessionLocal()
    post = db.query(Post).filter(Post.id == post_id).first()

    if not post:
        db.close()
        return jsonify({"error": f"Пост с id: {post_id} не найден !"}), 400

    data = request.get_json()
    title = data.get("title")
    if title is not None : post.title = title
    text = data.get("text")
    if text is not None : post.text = text
    db.commit()
    db.refresh(post)
    db.close()
    return jsonify({"message": "Данные обновлены !", "post": {"id": post.id, "title": post.title, "text": post.text}}), 200

@routes.route("/posts/<int:post_id>", methods = ["DELETE"])
def delete_user(post_id):
    db = SessionLocal()
    post = db.query(Post).filter(Post.id == post_id).first()

    if not post:
        db.close()
        return jsonify({"error": f"Пост с id: {post_id} не найден !"}), 400

    db.delete(post)
    db.commit()
    db.close()

    return jsonify({"message": f"Пост с id: {post_id} успешно удалён"}), 200