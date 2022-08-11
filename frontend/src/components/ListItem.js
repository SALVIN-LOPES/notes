import React from 'react'
import { Link } from 'react-router-dom'

let getTitle = (note) =>{
  let title = note.body.split('\n')[0]
  if(title.length > 45){
    return title.slice(0,45) + "..."
  }
  return title;
}

let getTime = (note) =>{
  return new Date(note.updated).toLocaleDateString()
}

let getContent = (note) =>{
  let title = getTitle(note)
  // console.log("title = ",title);
  let content = note.body.replaceAll('\n',' ')
  // console.log("content = ",content);
  content = content.replaceAll(title,'')
  // console.log("content after replace title = ",content);

  if(content.length > 45){
    return content.slice(0,45) + '....'
  }else{
    return content
  }
  
}

const ListItem = ({note}) => {

  return (
    <Link to={`/note/${note.id}`}>
      <div className='notes-list-item'>
        <h2>{getTitle(note)}</h2>
        <p><span>{getTime(note)}</span></p>
      </div>
    </Link>
  )
}

export default ListItem
