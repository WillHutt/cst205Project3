<!-- allows multiple file upload -->
<?php
if(isset($_FILES['files'])){
    $errors= array();
	foreach($_FILES['files']['tmp_name'] as $key => $tmp_name ){
		$file_name = $key.$_FILES['files']['name'][$key];
		$file_size =$_FILES['files']['size'][$key];
		$file_tmp =$_FILES['files']['tmp_name'][$key];
		$file_type=$_FILES['files']['type'][$key];	
        if($file_size > 2097152){
			$errors[]='File size must be less than 2 MB';
        }		
        $query="INSERT into pictures/ ('USER_ID','FILE_NAME','FILE_SIZE','FILE_TYPE') VALUES('$user_id','$file_name','$file_size','$file_type'); ";
        $desired_dir="pictures/";
        if(empty($errors)==true){
            if(is_dir($desired_dir)==false){
                mkdir("$desired_dir", 0700);		// Create directory if it does not exist
            }
            if(is_dir("$desired_dir/".$file_name)==false){
                move_uploaded_file($file_tmp,"pictures/".$file_name);
            }else{									//rename the file if another one exist
                $new_dir="pictures/".$file_name.time();
                 rename($file_tmp,$new_dir) ;				
            }
        }else{
                print_r($errors);
        }
    }
	if(empty($error)){
		echo "Success";
	}
}
?>