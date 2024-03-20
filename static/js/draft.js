document.addEventListener('DOMContentLoaded', function() {
    fetch_draft();
})


function fetch_draft() {
    let url = '/api/draft-blogs/';
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
            console.log("/" + parsedData[0].fields.image)
            if (parsedData) {
                fill_draft(parsedData)
            } else {
                console.log("there was no data to show")
            }
            
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
}


function fill_draft(data) {
    document.getElementById('title').value = data[0].fields.title;
    document.getElementById('summary').value = data[0].fields.summary;
    document.getElementById('content').value = data[0].fields.content;
    document.getElementById('heading').innerHTML = "You have a saved draft";
    const parentElement = document.getElementById('parentElementId');
    document.getElementById('heading_title').innerHTML = "Title: (Do not change the title of the draft post.)";

    element = document.getElementById('draft_check');
    if (element) {
        element.style.display = 'none';
    }
    const newButton = document.createElement('button');
    newButton.textContent = 'Delete draft'; 
    newButton.id = 'newButtonId'

    newButton.addEventListener('click', function() {
        
        window.location.href = `/delete_draft/${data[0].fields.title}`
    });
    parentElement.appendChild(newButton);
}