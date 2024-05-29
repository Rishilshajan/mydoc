import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.1/firebase-app.js";
  import { getAuth ,GoogleAuthProvider ,signInWithPopup } from "https://www.gstatic.com/firebasejs/10.12.1/firebase-auth.js";
  const firebaseConfig = {
    apiKey: "AIzaSyD6Lr8Nd9OQcMZTkRgVU7JDmpstKipgDFo",
    authDomain: "bookmydoc-3883e.firebaseapp.com",
    projectId: "bookmydoc-3883e",
    storageBucket: "bookmydoc-3883e.appspot.com",
    messagingSenderId: "304177341106",
    appId: "1:304177341106:web:fefe58d2dfdc7fc2d05fab"
  };

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
  const auth = getAuth(app);
  auth.languageCode = 'en';
  const provider = new GoogleAuthProvider();

  const googleLogin = document.getElementById("google-login-btn");
  googleLogin.addEventListener("click",function(){
    alert(5);
  }
  )

