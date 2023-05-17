// Config
$currentDirectory = getcwd();
$uploadDirectory = '/uploads/';
$fileExtensionsAllowed = ['jpeg', 'jpg', 'png']; // These will be the only file extensions allowed
$fileLimitMb = 5; // File limit in MB
$uploadOk = true;

$fileName = $_FILES['fileToUpload']['name'];
$fileSize = $_FILES['fileToUpload']['size'];
$fileTmpName  = $_FILES['fileToUpload']['tmpName'];
$fileType = $_FILES['fileToUpload']['type'];
$fileExtension = strtolower(end(explode('.', $fileName)));

$uploadPath = $currentDirectory . $uploadDirectory . basename($fileName);


move_uploaded_file($fileTmpName, $target_file)