# Image_Segmentation & Watermark_Removal
Full-stack image segmentation software (can also be used to remove watermark, but still needs some upgrade)
Divide an uploaded picture into as many segments as a number that you input according to the color

<h2>How I implemented this program</h2>
    <ul>
        <li>I used K-means clustering algorithm to cluster the pixels with similar colors. Then assign the mean color of each cluster to the corresponding pixels.</li>
        <li>To remove watermark, the algorithm is the same, except that the choice of initial points is non-random.</li>
        <ul><li>I think there are still a lot to work on. I only implement the gray situation.</li></ul>
    </ul>

<h2>Preview the effect</h2>
    <div>
        <h4>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For k=2:</h4>
            <img src="static/view.jpg" alt="BEFORE" height="250">
            <img src="static/view_2.jpg" alt="AFTER" height="250">
        <h4>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For k=5:</h4>
            <img src="static/view.jpg" alt="BEFORE" height="250">
            <img src="static/view_5.jpg" alt="AFTER" height="250">
        <h4>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For watermark removal:</h4>
            <img src="static/Watermark.jpg" alt="BEFORE" height="300">
            <img src="static/Watermark_after.jpg" alt="AFTER" height="300">
    </div>
