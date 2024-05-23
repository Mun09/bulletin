import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom"; // 리액트 라우터 임포트
import axios from "axios";

import "./Bulletin.css";

const Bulletin = () => {
  const [posts, setPosts] = useState([]);
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [editId, setEditId] = useState(null);

  useEffect(() => {
    fetchPosts();
  }, []);

  const fetchPosts = async () => {
    const response = await axios.get("http://localhost:8000/posts");
    setPosts(response.data);
  };

  const createPost = async () => {
    try {
        const postData = {
            id: null, // 서버에서 생성될 것이므로 일단 null로 설정합니다.
            title: title,
            content: content,
          };

        const response = await axios.post("http://localhost:8000/posts", postData);
        setPosts([...posts, response.data]);
        setTitle("");
        setContent("");
    } catch (error) {
        console.error("Error creating post:", error);
    }

  };

  const deletePost = async (id) => {
    await axios.delete(`http://localhost:8000/posts/${id}`);
    setPosts(posts.filter((post) => post.id !== id));
  };

  const updatePost = async () => {
    const updateData = {
      title,
      content
    }
    const response = await axios.patch(`http://localhost:8000/posts/${editId}`, updateData);
    setPosts(posts.map((post) => (post.id === editId ? response.data : post)));
    setTitle("");
    setContent("");
    setEditId(null);
  };

  return (
    <div className="bulletin-container">
      <h1>우리동네신문고</h1>
      <div className="input-container">
        <input
          type="text"
          placeholder="제목"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        <textarea
          placeholder="내용"
          value={content}
          onChange={(e) => setContent(e.target.value)}
        />
        {editId ? (
          <button className="edit" onClick={updatePost}>수정</button>
        ) : (
          <button onClick={createPost}>작성</button>
        )}
      </div>
      <ul>
        {posts.map((post) => (
          <li key={post.id} className="post-item">
            <h2>
              <Link to={`/posts/${post.id}`}>{post.title}</Link>
            </h2>
            <p>{post.content}</p>
            <button className="edit" onClick={() => {
              setTitle(post.title);
              setContent(post.content);
              setEditId(post.id);
            }}>수정</button>
            <button onClick={() => deletePost(post.id)}>삭제</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Bulletin;
