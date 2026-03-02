
/* ---------------------------------------------------------------
   CONFIGURAÇÕES GERAIS - SUBSTITUA COM SEUS DADOS
   ---------------------------------------------------------------
*/
const CLIENT_ID = '508604089670-0eg3u9eb46m2bvhprc6oe1hgdoidc7hd.apps.googleusercontent.com';  // <--- Cole seu ID aqui novamente
const API_KEY = 'SGOCSPX-k6xkOIHCBio267T4a4VXR0azfiPn';     // <--- Cole sua API Key aqui novamente

// Permissões necessárias (Criar e Gerir ficheiros)
const DISCOVERY_DOC = 'https://www.googleapis.com/discovery/v1/apis/drive/v3/rest';
const SCOPES = 'https://www.googleapis.com/auth/drive.file';

let tokenClient;
let gapiInited = false;
let gisInited = false;

/* ---------------------------------------------------------------
   PARTE 1: INICIALIZAÇÃO E LOGIN
   ---------------------------------------------------------------
*/

function gapiLoaded() {
    gapi.load('client', intializeGapiClient);
}

async function intializeGapiClient() {
    await gapi.client.init({ apiKey: API_KEY, discoveryDocs: [DISCOVERY_DOC] });
    gapiInited = true;
    updateButtonStatus();
}

function gisLoaded() {
    tokenClient = google.accounts.oauth2.initTokenClient({
        client_id: CLIENT_ID,
        scope: SCOPES,
        callback: '', // Será definido ao clicar
    });
    gisInited = true;
    updateButtonStatus();
}

function updateButtonStatus() {
    if (gapiInited && gisInited) {
        document.getElementById('auth-status').innerText = "Pronto para conectar.";
    }
}

function handleAuthClick() {
    tokenClient.callback = async (resp) => {
        if (resp.error !== undefined) throw (resp);
        
        // Sucesso
        document.getElementById('auth-status').innerText = "✅ Conectado ao Google Drive";
        document.getElementById('google-login-btn').style.display = 'none';
        
        // Verifica/Cria a pasta do Diário logo ao logar
        await findOrCreateFolder();
    };

    if (gapi.client.getToken() === null) {
        tokenClient.requestAccessToken({prompt: 'consent'});
    } else {
        tokenClient.requestAccessToken({prompt: ''});
    }
}

/* ---------------------------------------------------------------
   PARTE 2: LÓGICA DO DRIVE (PASTAS E UPLOADS)
   ---------------------------------------------------------------
*/

let folderId = null; // Vamos guardar o ID da pasta aqui

// Procura a pasta "Meu Diário Digital". Se não achar, cria.
async function findOrCreateFolder() {
    const folderName = "Meu Diário Digital";
    const query = `mimeType='application/vnd.google-apps.folder' and name='${folderName}' and trashed=false`;

    try {
        const response = await gapi.client.drive.files.list({
            q: query,
            fields: 'files(id, name)',
            spaces: 'drive'
        });

        const files = response.result.files;
        if (files && files.length > 0) {
            folderId = files[0].id;
            console.log("Pasta encontrada:", folderId);
        } else {
            // Cria a pasta
            const fileMetadata = {
                'name': folderName,
                'mimeType': 'application/vnd.google-apps.folder'
            };
            const folder = await gapi.client.drive.files.create({
                resource: fileMetadata,
                fields: 'id'
            });
            folderId = folder.result.id;
            console.log("Pasta criada:", folderId);
        }
    } catch (err) {
        console.error("Erro ao buscar pasta", err);
    }
}

// Função Principal de Salvar
async function saveToDrive() {
    // 1. Verifica login
    if (!gapi.client.getToken()) {
        alert("Por favor, faça login primeiro!");
        return;
    }
    
    // 2. Prepara os dados
    const title = document.getElementById('title-input').value || "Sem Titulo";
    const text = document.getElementById('text-input').value;
    const mediaInput = document.getElementById('media-upload');
    const statusMsg = document.getElementById('auth-status');

    statusMsg.innerText = "⏳ A enviar dados para o Drive...";

    try {
        // 3. Se tiver imagem/video, faz upload primeiro
        let mediaLink = "";
        if (mediaInput.files.length > 0) {
            const file = mediaInput.files[0];
            const mediaId = await uploadFileToDrive(file, folderId);
            mediaLink = `\n\n[Arquivo de Mídia anexado: Ver no Drive (ID: ${mediaId})]`;
        }

        // 4. Salva o texto (Diário)
        const textContent = `DATA: ${new Date().toLocaleString()}\nTÍTULO: ${title}\n\n${text}${mediaLink}`;
        const textBlob = new Blob([textContent], {type: 'text/plain'});
        const textFilename = `${title} - ${new Date().toLocaleDateString().replace(/\//g, '-')}.txt`;
        
        await uploadSimpleFile(textBlob, textFilename, folderId);

        statusMsg.innerText = "🎉 Memória salva com sucesso!";
        alert("Salvo na pasta 'Meu Diário Digital'!");

    } catch (error) {
        console.error(error);
        statusMsg.innerText = "❌ Erro ao salvar.";
        alert("Ocorreu um erro. Verifique o console (F12).");
    }
}

// Upload Genérico de Arquivos (Complexo, mas necessário para Binários)
async function uploadFileToDrive(file, parentFolderId) {
    const metadata = {
        'name': file.name,
        'parents': [parentFolderId] // Coloca dentro da pasta
    };

    const accessToken = gapi.client.getToken().access_token;
    const form = new FormData();
    
    form.append('metadata', new Blob([JSON.stringify(metadata)], { type: 'application/json' }));
    form.append('file', file);

    const res = await fetch('https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart', {
        method: 'POST',
        headers: new Headers({ 'Authorization': 'Bearer ' + accessToken }),
        body: form
    });
    
    const data = await res.json();
    return data.id; // Retorna o ID do arquivo salvo
}

// Upload Simples para Texto
async function uploadSimpleFile(blob, name, parentFolderId) {
    // Reutilizamos a mesma lógica pois funciona bem para texto também
    const file = new File([blob], name, { type: 'text/plain' });
    return await uploadFileToDrive(file, parentFolderId);
}

/* ---------------------------------------------------------------
   PARTE 3: INTERFACE (TEMA E PREVIEW)
   ---------------------------------------------------------------
*/

function toggleTheme() {
    const current = document.documentElement.getAttribute('data-theme');
    const target = current === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', target);
    localStorage.setItem('theme', target);
}

if (localStorage.getItem('theme') === 'dark') {
    document.documentElement.setAttribute('data-theme', 'dark');
}

function previewMedia(event) {
    const file = event.target.files[0];
    const previewContainer = document.getElementById('preview-container');
    previewContainer.innerHTML = ''; 

    if (file) {
        const objectUrl = URL.createObjectURL(file);
        if (file.type.startsWith('image/')) {
            const img = document.createElement('img');
            img.src = objectUrl;
            previewContainer.appendChild(img);
        } else if (file.type.startsWith('video/')) {
            const video = document.createElement('video');
            video.src = objectUrl;
            video.controls = true;
            previewContainer.appendChild(video);
        }
    }
}