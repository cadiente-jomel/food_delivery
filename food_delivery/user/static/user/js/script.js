// ajax for upload
'use-strict';

//CSRFToken
const getCookie = (name) => {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');
// CSRFToken
const profileUpload = () => {

    const firstName = document.getElementById('id_first_name')
    const lastName = document.getElementById('id_last_name')
    let data = {
        firstName: firstName.value,
        lastName: lastName.value,
    }
    fetch('/profile_upload/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify(data)
    }).then(response => {
        return response.json();
    }).then(result => {
        console.log(result);
    });
}

const eventListener = () => {
    const form = document.getElementById('form');

    form.addEventListener('submit', e => {
        e.preventDefault();
        profileUpload();
    });
}

eventListener();
