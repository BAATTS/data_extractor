var _require = require('child_process'),
    spawn = _require.spawn; // Extract bookmarked data from word files


// function extract_data_doc() {
var childPython = spawn('python', ['doc_to_docx.py']);
childPython.stdout.on('data', function (data) {
    console.log("stdout: ".concat(data));
});
childPython.stderr.on('data', function (data) {
    console.error("stderr: ".concat(data));
});
childPython.on('close', function (code) {
    console.log("child process exited with code ".concat(code));
});
// }

// module.exports.extract_data_doc = extract_data_doc;