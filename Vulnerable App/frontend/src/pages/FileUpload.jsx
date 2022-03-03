const FileUpload = () => {
    return (
        <div>
            <div className="justify-around m-6">
                <h1 className="text-4xl">File Upload</h1>
                <div className="my-3 bg-dvma5 py-2 px-4">
                    <h3 className="text-sm">Choose an Image to upload</h3>
                    <form action="" className="my-4 flex flex-col">
                        <input type="file" className="mx-2" />
                        <button className="btn">Upload</button>
                    </form>
                </div>
            </div>
        </div>
    );
};

export default FileUpload;
