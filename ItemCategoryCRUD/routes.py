from flask import Blueprint, request, jsonify
from models import Item, Category
from config import db

api = Blueprint('api', __name__)

@api.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    if not items:
        return jsonify({"message": "No items found"}), 404
    return jsonify([{
        "id": item.id,
        "name": item.name,
        "price": item.price,
        "category_id": item.category_id
    } for item in items]), 200

@api.route('/items/<int:id>', methods=['GET'])
def get_item(id):
    item = Item.query.get(id)
    if not item:
        return jsonify({"message": "No item found"}), 404
    return jsonify({
        "id": item.id,
        "name": item.name,
        "price": item.price,
        "category_id": item.category_id
    }), 200

@api.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    new_item = Item(
        name=data.get('name'),
        price=data.get('price'),
        category_id=data.get('category_id')
    )
    db.session.add(new_item)
    db.session.commit()
    return jsonify({
        'id': new_item.id,
        'name': new_item.name,
        'price': new_item.price,
        'category_id': new_item.category_id
    }), 201

@api.route('/items/<int:id>', methods=['PUT'])
def update_item(id):
    data = request.get_json()
    item = Item.query.get(id)
    if not item:
        return jsonify({"message": "No item found to delete"}), 404
    item.name = data.get('name', item.name)
    item.price = data.get('price', item.price)
    item.category_id = data.get('category_id', item.category_id)
    db.session.commit()
    return jsonify({'message': 'Item updated!'}), 200

@api.route('/items/<int:id>', methods=['DELETE'])
def delete_item(id):
    item = Item.query.get(id)
    if not item:
        return jsonify({"message": "No item found to delete"}), 404
    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'item deleted!'}), 200

@api.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    if not categories:
        return jsonify({"message": "Categories not found!"}), 404
    return jsonify([{
        "id": category.id,
        "name": category.name
    } for category in categories]), 200

@api.route('/categories/<int:id>', methods=['GET'])
def get_category(id):
    category = Category.query.get(id)
    if not category:
        return jsonify({"message": "Category not found!"}), 404
    return jsonify({
        'id': category.id,
        'name': category.name
    }), 200

@api.route('/categories', methods=['POSt'])
def create_category():
    data = request.get_json()
    new_category = Category(name=data.get('name'))
    db.session.add(new_category)
    db.session.commit()
    return jsonify({'id': new_category.id, 'name': new_category.name}), 201

@api.route('/categories/<int:id>', methods=['PUT'])
def update_category(id):
    data = request.get_json()
    category = Category.query.get(id)
    if not category:
        return jsonify({"message": "Category not found to delete!"}), 404
    category.name = data.get('name', category.name)
    db.session.commit()
    return jsonify({"message": "category updated!"}), 200

@api.route('/categories/<int:id>', methods=['DELETE'])
def delete_category(id):
    category = Category.query.get(id)
    if not category:
        return jsonify({"message": "Category not found to delete!"}), 404
    db.session.delete(category)
    db.session.commit()
    return jsonify({"message": "Category deleted!"}), 200