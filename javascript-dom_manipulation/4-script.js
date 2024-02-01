const listItem = document.getElementById('add_item');

listItem.addEventListener('click', function() {
const newItem = document.createElement('li')

newItem.textContent = 'Item';

const list = document.querySelector('.my_list');

list.appendChild(newItem);
});
