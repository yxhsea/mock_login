
function decryption(encryptedBase64Str){
    let key = "cmmgfgehahweuuii"
    let k = CryptoJS.enc.Utf8.parse(key)
    const decryptedData = CryptoJS.AES.decrypt(encryptedBase64Str, k, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    });
    return pako.ungzip(O(decryptedData), {to: "string"});
}

function O(t) {
    let e, n, a = t.words.length, i = new Uint8Array(t.sigBytes), r = 0;
    for (n = 0; n < a; n++)
        e = t.words[n],
            i[r++] = e >> 24,
            i[r++] = e >> 16 & 255,
            i[r++] = e >> 8 & 255,
            i[r++] = 255 & e;
    return i
}
