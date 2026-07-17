console.log("Script loaded OK");

// ===== DOM =====
let bubble, btnTalk, btnStop, btnStory, btnMusic, bgm;

// ===== STATE =====
let isTalking = false;
let isRecognizing = false;
let isMusicPlaying = false;
let mode = "idle"; // idle | talk | story
let storyIndex = 0;

const storyLines = [
`Chào bé yêu…

Đêm đã xuống rồi…
Ngoài sân…
gió thổi rất nhẹ…

Robot kể cho bé nghe
một câu chuyện nhỏ…
để bé dễ ngủ nhé…

Ngày xưa…
ở một ngôi nhà nhỏ nơi làng quê…
có một chú mèo con màu vàng nhạt
sống cùng bà và bếp lửa hồng.

Mỗi buổi chiều…
khi mặt trời dần tắt…
bà lại nhóm bếp…
nấu nồi cơm thơm…

Chú mèo cuộn tròn bên bếp…
nghe tiếng củi cháy tí tách…
cảm thấy rất ấm…

Buổi tối hôm đó…
trời se lạnh hơn…
trăng treo lơ lửng trên mái nhà…

Chú mèo nhỏ bước ra hiên…
nhìn cánh đồng xa xa…
nghe tiếng ếch kêu ngoài mương…

Một làn gió nhẹ thổi qua…
mang theo mùi rơm khô…
và hương lúa chín…

Chú mèo quay vào nhà…
nằm sát bên bếp lửa…

Bà nhẹ nhàng vuốt lưng chú…
giọng bà hiền và ấm…

Ngủ đi mèo nhỏ…
đêm là để nghỉ ngơi…

Chú mèo khẽ khẽ dụi đầu…
đuôi khẽ khẽ đung đưa…

Ngoài kia…
tiếng dế gáy rả rích…
tiếng gió ru hàng tre…

Bếp lửa vẫn hồng…
soi bóng chú mèo ngủ yên…

Mắt chú khép lại…
thở đều…
ngủ thật ngoan…

Bé yêu à…
bây giờ bé cũng vậy nhé…

Hãy nằm thật yên…
nhắm mắt lại…
nghe giọng robot chậm dần…

Hơi thở nhẹ hơn…
cơ thể thả lỏng…

Chúc bé ngủ thật ngon…
mơ những giấc mơ êm ái…

Ngủ ngoan nhé bé yêu.`,
];

// ===== REPLIES =====
const replies = {
  hello: [
    "Chào bé yêu!",
    "Robot rất vui khi nghe bé nói."
  ],
  sad: [
    "Robot ở đây với bé.",
    "Bé ôm robot một cái nhé."
  ],
  sleep: [
    "Robot ru bé ngủ nhé.",
    "Nhắm mắt lại và nghe robot kể chuyện nào."
  ],
  story: [
    "Ngày xưa có một chú mèo nhỏ rất ngoan.",
    "Có một ngôi sao bé xíu thích ngắm trăng."
  ],
  default: [
    "Robot đang lắng nghe bé.",
    "Bé nói tiếp đi."
  ]
};

// ===== SPEECH RECOGNITION =====
let recognition;

function initRecognition() {
  const SpeechRecognition =
    window.SpeechRecognition || window.webkitSpeechRecognition;

  recognition = new SpeechRecognition();
  recognition.lang = "vi-VN";
  recognition.continuous = false;        // 🔒 RẤT QUAN TRỌNG
  recognition.interimResults = false;

  recognition.onresult = (event) => {
    const text = event.results[0][0].transcript.toLowerCase();
    bubble.innerText = "👶 Bé nói: " + text;

    const reply = getReply(text);
    speak(reply);
  };

  recognition.onerror = () => {
    isRecognizing = false;
  };

  recognition.onend = () => {
    isRecognizing = false;
  };
}

// ===== SPEAK =====
function speak(text, resumeListening = false) {
  if (isRecognizing) {
    recognition.stop();
    isRecognizing = false;
  }

  speechSynthesis.cancel();
  const utter = new SpeechSynthesisUtterance(text);
  utter.lang = "vi-VN";

 utter.onend = () => {
  if (mode === "story") {
    setTimeout(nextStory, 500);
  }

  if (resumeListening && mode === "talk") {
    startRecognition();
  }
};

  speechSynthesis.speak(utter);
}

// ===== MIC CONTROL =====
function startRecognition() {
  if (isRecognizing) return;
  recognition.start();
  isRecognizing = true;
}

// ===== TALK BUTTONS =====
function startTalk() {
  if (isTalking) return;

  mode = "talk";
  isTalking = true;
  bubble.innerText = "🎤 Robot đang lắng nghe bé...";
  startRecognition();
}

function stopTalk() {
  isTalking = false;

  if (isRecognizing) {
    recognition.stop();
    isRecognizing = false;
  }

  speechSynthesis.cancel();

  bubble.innerText = "⏸ Robot tạm nghỉ nhé!";
}

// ===== STORY =====
function tellStory() {
  stopTalk();

  mode = "story";
  storyIndex = 0;

  bubble.innerText = "📖 Robot đang kể chuyện cho bé...";
  speak(storyLines[storyIndex]);
}
function nextStory() {
  storyIndex++;

  if (storyIndex < storyLines.length) {
    speak(storyLines[storyIndex]);
  } else {
    mode = "idle";
  }
}
window.startAutoStory = function () {
  tellStory();
};

// ===== MUSIC =====
function toggleMusic() {
  if (!bgm) return;

  if (bgm.paused) {
    bgm.play().catch(() => {});
    btnMusic.innerText = "⏸ DỪNG NHẠC";
    isMusicPlaying = true;
  } else {
    bgm.pause();
    btnMusic.innerText = "🎵 NHẠC RU";
    isMusicPlaying = false;
  }
}


// ===== LOGIC =====
function getReply(text) {
  if (text.includes("chào")) return random(replies.hello);
  if (text.includes("buồn") || text.includes("khóc")) return random(replies.sad);
  if (text.includes("ngủ") || text.includes("mệt")) return random(replies.sleep);
  if (text.includes("kể") || text.includes("chuyện"))
    return random(replies.story);

  return random(replies.default);
}

function random(arr) {
  return arr[Math.floor(Math.random() * arr.length)];
}

// ===== INIT =====
document.addEventListener("DOMContentLoaded", () => {
  bubble   = document.getElementById("bubble");
  btnTalk  = document.getElementById("btnTalk");
  btnStop  = document.getElementById("btnStop");
  btnStory = document.getElementById("btnStory");
  btnMusic = document.getElementById("btnMusic");
  bgm      = document.getElementById("bgm");

  initRecognition();

  btnTalk.onclick  = startTalk;
  btnStop.onclick  = stopTalk;
  btnStory.onclick = tellStory;
  btnMusic.onclick = toggleMusic;
});
