<script>
    export let message = 'Loading...';
 </script>
 
 <div class="loading-screen">
    <div class="spinner"></div>
    <p>{message}</p>
 </div>
 
 <style>
    .loading-screen {
       position: fixed;
       top: 0;
       left: 0;
       width: 100%;
       height: 100%;
       background: rgba(255, 255, 255, 0.9);
       display: flex;
       flex-direction: column;
       justify-content: center;
       align-items: center;
       z-index: 9999;
    }
 
    .spinner {
       width: 50px;
       height: 50px;
       border: 4px solid rgba(0, 0, 0, 0.1);
       border-top-color: #024D98;
       border-radius: 50%;
       animation: spin 1s linear infinite;
    }
 
    @keyframes spin {
       from {
          transform: rotate(0deg);
       }
       to {
          transform: rotate(360deg);
       }
    }
 
    p {
       margin-top: 10px;
       font-size: 1.2rem;
       color: #333;
       font-family: coolvetica;
    }
 </style>
 