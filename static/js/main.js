let searchForm = document.getElementById('searchForm')

  let pageLinks = document.getElementsByClassName('page-link')


  if(searchForm){
    for(let i=0 ; pageLinks.length>i ; i++){

      pageLinks[i].addEventListener('click', function(e){
        
        e.preventDefault()
        let page= this.dataset.page
        
        searchForm.innerHTML += `<input value=${page} name="page" hidden />`
        searchForm.submit()
      })
    }
  }

let tagButtons=document.getElementsByClassName("tag-form")

  for(let i=0 ;tagButtons.length>i ; i++){

    tagButtons[i].addEventListener('click', function(e){
      tagName=this.dataset.tag
      projectID=this.dataset.project
      linkDelete='http://127.0.0.1:8000/projects/update-project/' + projectID +'/tag&deletion/'+ tagName

      fetch(linkDelete)
      .then(
        tagButtons[i].remove()
      )
    })
  }