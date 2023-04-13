function deleteObject(pk){
    var link = "http://127.0.0.1:8000/projects/delete-project/";
    link += pk;
   
    console.log(link)
    Swal.fire({
    title: `Are you sure to delete ${pk}?`,
    text: "You won't be able to revert this!",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Yes, delete it!'
  }).then((result) => {
    if (result.isConfirmed) {
      location = link;
    }
  })
  
  }