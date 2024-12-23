let progress = document.getElementById("progress");
let song = document.getElementById("audioPlayer");
let ctrlIcon = document.getElementById("ctrlIcon");

document.addEventListener('DOMContentLoaded', function () {
    var audioPlayer = document.getElementById('audioPlayer');

    document.querySelectorAll('.play-button').forEach(function (button) {
        button.addEventListener('click', function (event) {
            event.preventDefault();
            var song_name = this.closest('.card').querySelector('#song_data_name').innerText;
            var song_artist = this.closest('.card').querySelector('#song_data_artist').innerText;
            document.getElementById('player_song_name').innerText = song_name;
            document.getElementById('player_artist_name').innerText = song_artist;
            var songUrl = this.getAttribute('data-song-url');
            audioPlayer.src = songUrl;
            audioPlayer.play();
            ctrlIcon.classList.remove("fa-play");
            ctrlIcon.classList.add("fa-pause");
        });
    });
});

song.onloadedmetadata = function () {
    progress.max = song.duration;
    progress.value = song.currentTime;
}

function playPause() {
    if (ctrlIcon.classList.contains("fa-pause")) {
        song.pause();
        ctrlIcon.classList.remove("fa-pause");
        ctrlIcon.classList.add("fa-play");
    } else {
        song.play();
        ctrlIcon.classList.remove("fa-play");
        ctrlIcon.classList.add("fa-pause");
    }
}

if (song.play) {
    setInterval(() => {
        progress.value = song.currentTime;
    }, 100);
}

progress.onchange = function () {
    song.play();
    song.currentTime = progress.value;
    ctrlIcon.classList.remove("fa-play");
    ctrlIcon.classList.add("fa-pause");
}