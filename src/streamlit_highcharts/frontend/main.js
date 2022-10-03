function sendValue(value) {
  Streamlit.setComponentValue(value)
}


function onRender(event) {
  if (!window.rendered) {
    const {options,height} = event.detail.args
    Streamlit.setFrameHeight(height+20)
    document.getElementById("container").style.height=height+"px"
    Highcharts.chart('container', options);
    window.rendered = true
  }
}

Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)
Streamlit.setComponentReady()
