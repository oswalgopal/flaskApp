document.addEventListener('DOMContentLoaded', () => {
    // connnection to web sockets
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    socket.on('connect', () => {
        console.log('connected to the socket');
        document.querySelector('#form').onsubmit = () => {
            const message = document.getElementById('message').value;
            socket.emit('message', { 'message': message });
            document.getElementById('message').value = '';
            return false
        }
    })
    socket.on('messageAll', data => {
        console.log(data);
        const li = document.createElement('li');
        li.innerHTML = data;
        document.getElementById('messageList').append(li);
    });
})