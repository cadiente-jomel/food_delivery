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
    const addressBtn = document.querySelector('.address__btn');
    const addressForm = document.querySelector('.address__form');
    const profileEditBtn = document.querySelectorAll('.profile__edit');

    const lastName = document.getElementById('id_first_name');
    const firstName = document.getElementById('id_last_name');

    form.addEventListener('submit', e => {
        e.preventDefault();
        profileUpload();
    });

    addressBtn.addEventListener('click', e => {
        if(addressForm.classList.contains('active')) {
            addressBtn.innerHTML = `Add address`
            addressForm.classList.add('d-none')
            addressForm.classList.remove('active');
            addressBtn.innerHTML = `<i class="fas fa-plus"></i> Add Address`
        } else {
            addressBtn.innerHTML = `<i class="fas fa-times"></i> Cancel`
            addressForm.classList.add('active')
            addressForm.classList.remove('d-none');
            addressForm.style.display = 'flex';

        }
    });

    profileEditBtn.forEach(btn => {
        btn.addEventListener('click', () => {
            if(btn.classList.contains('enable')) {
                btn.classList.remove('enable');
                
                btn.previousElementSibling.children[0].disabled = true;
            } else {
                btn.classList.add('enable');
                btn.previousElementSibling.children[0].disabled = false;
            }
        });
    });

}

eventListener();
