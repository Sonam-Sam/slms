const menuToggle = document.querySelector('.menu-toggle1');
const navigation = document.querySelector('.navigation1');

menuToggle.onclick = () => {
    navigation.classList.toggle('open')
}

const listItems = document.querySelectorAll('.list-item1');

listItems.forEach(item => {
    item.onclick = () => {
        listItems.forEach(item => 
        item.classList.remove('active'));
        item.classList.add('active');
    }
})