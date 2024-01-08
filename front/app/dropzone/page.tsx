"use client"

import { useCallback, useMemo } from 'react';
import { useDropzone, FileWithPath } from 'react-dropzone';

const baseStyle = {
    width: 200,
    height: 150,
};
const borderNormalStyle = {
    border: "1px dotted #888"
};
const borderDragStyle = {
    border: "1px solid #00f",
    transition: 'border .5s ease-in-out'
};
function App() {
    
    const onDrop = useCallback((acceptedFiles) => {
        console.log('acceptedFiles:', acceptedFiles);
        // file = acceptedFiles;
    }, []);
    
    const { getRootProps, getInputProps, isDragActive, open, acceptedFiles } = useDropzone({ onDrop });
    const style = useMemo(() => (
        { ...baseStyle, ...(isDragActive ? borderDragStyle : borderNormalStyle)}
    ), [isDragActive]);
    const filesUpdate: FileWithPath[] = acceptedFiles;
    const files = useMemo(() => 
        filesUpdate.map(file => (
            <li key={file.path}>
                {file.path} - {file.size} bytes
            </li>
        )
    ), [acceptedFiles]);
    return (
        <div>
            <div {...getRootProps({ style })}>
                {/* Imageのみ可 */}
                <input type="file" accept="image/*"{...getInputProps()} />
                {
                    isDragActive ?
                        <p>Drop the files here ...</p> :
                        <p>ここに画像をドラッグ・アンド・ドロップしてください。</p>
                }
            </div>
                <button type="button" onClick={open}>画像を選択</button>
            <aside>
                <h4>Files</h4>
                <ul>{files}</ul>
            </aside>
        </div>
    );
    
}

export default App;
