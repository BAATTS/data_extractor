const { spawn } = require('child_process');


// Extract bookmarked data from word files
function extract_data_doc() {
    const childPython = spawn('python', ['doc_to_docx.py']);

    childPython.stdout.on('data', (data) => {
        console.log(`stdout: ${data}`);
    });

    childPython.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
    });

    childPython.on('close', (code) => {
        console.log(`child process exited with code ${code}`);
    });
}

module.exports.extract_data_doc = extract_data_doc;