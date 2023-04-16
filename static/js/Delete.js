function deleteObject(pk , num){
   console.log(num)

   if(num==1){
    link='http://127.0.0.1:8000/delete_skill/'
   }
   else if(num==2){
    link='http://127.0.0.1:8000/projects/delete-project/'
   }
   else if(num==3){
    link='http://127.0.0.1:8000/projects/review/delete/'

   }
   else{
    link=null
   }
    
    
    link += pk;
   
    console.log(link)
    Swal.fire({
    title: 'Are you sure to delete this item',
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