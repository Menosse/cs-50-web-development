document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);
  
  // By default, load the inbox
  load_mailbox('inbox');

  // Submit email
  document.querySelector('#compose-form').addEventListener('submit', send_email);
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#single-email-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#single-email-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
  get_emails(mailbox)
}

function send_email(){
  event.preventDefault();
  fetch('/emails', {
    method: 'POST',
    body: JSON.stringify({
        recipients: document.querySelector('#compose-recipients').value,
        subject: document.querySelector('#compose-subject').value,
        body: document.querySelector('#compose-body').value
    })
  })
  .then(response => response.json())
  .then(result => {
    console.log(result);
    load_mailbox('sent')
  })
  .catch(error => {
    console.log("Error", error);
  })
}

function get_emails(mailbox){
  console.log(`/emails/${mailbox}`)
  fetch(`/emails/${mailbox}`)
    .then(response => response.json())
    .then(result =>{
      result.forEach(email => {
        const email_div = document.createElement('div');
        email_div.innerHTML = `<a>${email.sender} ${email.subject} ${email.timestamp}</a>`;
        email_div.addEventListener('click', () => {
          single_email(email)
          if(!email.read){
            read(email)
          }
        })
        if(!email.read){
          email_div.style.background = 'white';
          email_div.style.fontWeight = 'bold';
        } else {
          email_div.style.background = 'lightgrey'
        }
        document.querySelector('#emails-view').append(email_div)
      });
    })
    .catch(error =>{
      console.log("Error", error)
    })
  }


function single_email(email){
  console.log(email)
  fetch(`/emails/${email.id}`)
  .then(response => response.json())
  .then(result=>{
    console.log(result.sender)
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'none';
    document.querySelector('#single-email-view').style.display = 'block';
    
    
    // Subject - create HTML element
    document.querySelector('#single-email-view').innerHTML = `<h3>Subject: ${result.subject}</h3>`;

    // Sender - create HTML element
    const sender_div = document.createElement('div');
    sender_div.innerHTML = `From: ${result.sender}`
    document.querySelector('#single-email-view').append(sender_div)

    // Recipents - create HTML element
    const recipients_div = document.createElement('div');
    recipients_div.innerHTML = `To: ${result.recipients}`
    document.querySelector('#single-email-view').append(recipients_div)

    // Body - create HTML element
    const body_div = document.createElement('div');
    body_div.innerHTML = `Content: ${result.body}`
    document.querySelector('#single-email-view').append(body_div)

    // Timestamp - create HTML element
    const timestamp_div = document.createElement('div');
    timestamp_div.innerHTML = result.timestamp
    document.querySelector('#single-email-view').append(timestamp_div)

    //Check archived
    const archive_div = document.createElement('div');
    if(email.archived){
      archive_div.innerHTML = '<a href="">Move to inbox</a>';
    }else{
      archive_div.innerHTML = '<a href="">Archive email</a>';
    }
      archive_div.addEventListener('click',() => archive(email));
      document.querySelector('#single-email-view').append(archive_div)
    
      // Reply button
      const reply_div = document.createElement('div')
      reply_div.innerHTML = "<button class = \"btn btn-primary\">Reply</button>"
      reply_div.addEventListener('click',() => {
        reply_email(email)
      })
      document.querySelector('#single-email-view').append(reply_div)
  }).catch(error =>{
    console.log("Error", error)
  })
}

function archive(email){
  fetch(`/emails/${email.id}`, {
    method: 'PUT',
    body: JSON.stringify({
        archived: !email.archived
    })
  })
}

function read(email){
  fetch(`/emails/${email.id}`, {
    method: 'PUT',
    body: JSON.stringify({
        read: !email.read
    })
  })
}

function reply_email(email) {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#single-email-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Fill reply information
  document.querySelector('#compose-recipients').value = email.sender;
  
  if(email.subject.includes("Re:")){
    document.querySelector('#compose-subject').value = email.subject;
  }else{
    document.querySelector('#compose-subject').value = `Re: ${email.subject}` ;
  }
  document.querySelector('#compose-body').value = `\nOn ${email.timestamp} ${email.sender} wrote: \n ${email.body}`;
}