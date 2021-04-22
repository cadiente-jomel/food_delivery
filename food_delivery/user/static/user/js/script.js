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

// AJAX
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

const addAddress = () => {
    const form = document.querySelector('.form__add');
    let formData= new FormData(form);
    let data = {};

    for(let d of formData) {
        data[d[0]] = d[1];
    }

    if(data['note'].length === 0) {
        data['note'] = null;
    }

    fetch('/add_address/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify(data)
    })
        .then(response => {
            return response.json();
        })
        .then(result => {
            let addressData = JSON.parse(result.data);
            console.log(resutl.message);
        });

}

// AJAX

const eventListener = () => {
    const form = document.getElementById('form');
    const addressBtn = document.querySelector('.address__btn');
    const addressForm = document.querySelector('.address__form');

    const formAdd = document.querySelector('.form__add')

    const lastName = document.getElementById('id_first_name');
    const firstName = document.getElementById('id_last_name');

    const profileSave = document.querySelector('.profile__save');
    const profileEdit = document.querySelector('.edit__btn');

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

    profileEdit.addEventListener('click', () => {
        if (profileEdit.classList.contains('edit')) {
            profileSave.style.backgroundColor = '#9796AA';
            profileSave.disabled = true;
            profileEdit.classList.remove('edit');
            profileEdit.innerHTML = 'Edit';

            firstName.disabled = true;
            lastName.disabled = true;
        } else {
            profileSave.style.backgroundColor = 'var(--primary-color)';
            profileSave.disabled = false;
            profileEdit.innerHTML = `<i class="fas fa-times"></i>`;
            profileEdit.classList.add('edit');

            firstName.disabled = false;
            lastName.disabled = false;
        }
    })

    formAdd.addEventListener('submit', e => {
        e.preventDefault();

        addAddress();
    });

}

eventListener();
