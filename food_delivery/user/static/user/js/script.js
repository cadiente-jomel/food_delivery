// ajax for upload
'use-strict';

const popupSave = (text) => {
    const productSuccess = document.querySelector('.product__success');
    productSuccess.innerHTML = text;
    productSuccess.style.top = '0'; 
    setTimeout(() => {
        productSuccess.style.top = '-3.4rem';
    }, 7000);
}

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

const newAddressRender = (data) => {
    const tableBody = document.getElementById('table-body');

    let { full_name, phone, house_no, zip_code, province, city_municipality, barangay  } = data;

    let tableRow = `
              <tr>
                <th scope="row">${full_name}</th>
                <td>${house_no} ${barangay} ${city_municipality} ${province}</td>
                <td>${zip_code}</td>
                <td>${phone}</td>
                <td><a href="#">Edit</a></td>
              </tr>
    `;

    tableBody.innerHTML += tableRow;
}

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
        popupSave(result.message);
    });
}

const addAddress = () => {
    const addressSubmit = document.querySelector('.address__submit');
    const productSuccess = document.querySelector('.product__success');
    const form = document.querySelector('.form__add');
    let formData= new FormData(form);
    let data = {};

    for(let d of formData) {
        data[d[0]] = d[1];
    }

    if(data['note'].length === 0) {
        data['note'] = null;
    }

    if(addressSubmit.getAttribute('data-btn') === 'add') {
    

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
                newAddressRender(addressData);
                popupSave(result.message);
            });
    } else {


        let addId = addressSubmit.getAttribute('data-id');

        fetch(`/edit_address/${addId}/`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify(data)
        })
            .then(response => {
                return response.json()
            })
            .then(result => {
                let text = `${result.message} <a href="/profile/" style="color: #fff;">Reload</a> to see changes.`
                popupSave(text)
            })
    }


}

const editAddress = (data=false) => {
    const addressForm = document.querySelector('.address__form');
    const addressBtn = document.querySelector('.address__btn');

    const addressSubmit = document.querySelector('.address__submit');

    if(data) {


        let { fields } = JSON.parse(data);

        let { full_name, phone, note, house_no, zip_code, province, city_municipality, barangay  } = fields

        const customerFullName = document.getElementById('id_full_name');
        const customerPhone = document.getElementById('id_phone');
        const customerNote = document.getElementById('id_note');
        const customerHouseNo = document.getElementById('id_house_no');

        const customerZipCode = document.getElementById('id_zip_code');
        const customerProvince = document.getElementById('id_province');
        const customerCityMunicipality = document.getElementById('id_city_municipality');
        const customerBarangay = document.getElementById('id_barangay');


        customerFullName.value = full_name;
        customerPhone.value = phone;
        customerNote.value = note;
        customerHouseNo.value = house_no;
        customerZipCode.value = zip_code;
        customerProvince.value = province;
        customerCityMunicipality.value = city_municipality;
        customerBarangay.value = barangay;

    }

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
}

// AJAX

const eventListener = () => {
    const form = document.getElementById('form');
    const addressBtn = document.querySelector('.address__btn');
    const addressForm = document.querySelector('.address__form');

    const addressSubmit = document.querySelector('.address__submit');

    const formAdd = document.querySelector('.form__add')

    const lastName = document.getElementById('id_first_name');
    const firstName = document.getElementById('id_last_name');

    const profileSave = document.querySelector('.profile__save');
    const profileEdit = document.querySelector('.edit__btn');

    const editBtn = document.querySelectorAll('.edit-address');

    form.addEventListener('submit', e => {
        e.preventDefault();
        profileUpload();
    });

    addressBtn.addEventListener('click', e => {

        const customerFullName = document.getElementById('id_full_name');
        const customerPhone = document.getElementById('id_phone');
        const customerNote = document.getElementById('id_note');
        const customerHouseNo = document.getElementById('id_house_no');

        const customerZipCode = document.getElementById('id_zip_code');
        const customerProvince = document.getElementById('id_province');
        const customerCityMunicipality = document.getElementById('id_city_municipality');
        const customerBarangay = document.getElementById('id_barangay');

        customerFullName.value = null;
        customerPhone.value = null;
        customerNote.value = null;
        customerHouseNo.value = null;
        customerZipCode.value = null;
        customerProvince.value = null;
        customerCityMunicipality.value = null;
        customerBarangay.value = null

        addressSubmit.setAttribute('data-btn', 'add');

        if(addressSubmit.getAttribute('data-id')) {
            addressSubmit.removeAttribute('data-id');
        }
        editAddress();


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

    editBtn.forEach(btn => {
        btn.addEventListener('click', async function() {

            let dataId = this.getAttribute('data-id');

            let data =  await fetch(`/fetch_address/${dataId}/`);

            let response = await data.json();


            addressSubmit.setAttribute('data-btn', 'edit')
            addressSubmit.setAttribute('data-id', dataId)

            editAddress(response);
        })
    });

}

eventListener();
