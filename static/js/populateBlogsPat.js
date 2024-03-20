
document.addEventListener('DOMContentLoaded', function() {
    const categorySelect = document.getElementById('categorySelect');
    const blogList = document.getElementById('blogList');

    categorySelect.addEventListener('change', function() {
        const selectedCategory = categorySelect.value;
        fetchBlogs(selectedCategory);
    });
 
    function fetchBlogs(category) {
        let url = '/api/all-blog-posts/';
        if (category) {
            url += `?category=${category}`;
        }

        fetch(url)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                const modelData = data.data;
                const parsedData = JSON.parse(modelData);
                console.log(parsedData[0].fields)
                renderBlogs(parsedData, category);
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
            });
    }

 
    function renderBlogs(blogPosts, selectedCategory) {
        blogList.innerHTML = ''; 
        blogPosts.forEach(post => {
            console.log(post.fields.category)
            if (!selectedCategory || post.fields.category === selectedCategory) {
                const blogItem = document.createElement('li');
                blogItem.innerHTML = `
                    <h2>${post.fields.title}</h2>
                    <img src="/${post.fields.image}" alt="${post.title}">
                    <p>${post.fields.summary}</p>
                    <p>Category: ${post.fields.category}</p>
                    <p>Author: ${post.fields.name}</p>
                `;
                
              
                blogList.appendChild(blogItem);
            }
        });

       
        if (blogList.innerHTML === '') {
            blogList.innerHTML = `<li>No blog posts available for selected category.</li>`;
        }
    }

 
    fetchBlogs('Mental Health');
});
