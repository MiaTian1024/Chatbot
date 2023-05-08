
const img = "https://picsum.photos/200";

<div>
    <img alt="random" src={img} />
</div>

function Heading() {
    const date = new Date();
    const currentTime = date.getHours();
  
    let greeting;
  
    let customStyle = {
      color: ""
    };
  
    if (currentTime < 12) {
      greeting = "Good Morning";
      customStyle.color = "red";
    } else if (currentTime < 18) {
      greeting = "Good Afternoon";
      customStyle.color = "green";
    } else {
      greeting = "Good Night";
      customStyle.color = "blue";
    }
  
    return (
      <h1 className="heading" style={customStyle}>
        {greeting}
      </h1>
    );
  }