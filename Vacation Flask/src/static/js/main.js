
// Check if the admin sure about deleting vacation
function confirmDelete() {
    const ok = confirm("Are you sure you want to delete?");
    if (!ok) event.preventDefault();
}

// Like / Unlike Configuration
function isLiked(vacation_id) {
    console.log("Like button clicked for vacation ID:", vacation_id);
    
    const like = document.getElementById(`like-${vacation_id}`);
    console.log("Like button element:", like);
    
    const heart = document.getElementById(`heart-${vacation_id}`);
    console.log("Heart icon element:", heart);
    
    const isLiked = sessionStorage.getItem(`is_liked_${vacation_id}`);
    console.log("Is liked:", isLiked);

    if (isLiked === "true") {
        console.log("Vacation is already liked, unliking...");
        // Button is already liked, so unlike it
        like.classList.remove('liked'); // Remove liked class
        like.style.backgroundColor = "gray";
        heart.style.color = "wheat";
        sessionStorage.removeItem(`is_liked_${vacation_id}`);
        updateLikeCount(vacation_id, -1); // Decrement like count by 1
    } else {
        console.log("Vacation is not yet liked, liking...");
        // Button is not liked, so like it
        like.classList.add('liked'); 
        like.style.backgroundColor = "pink";
        heart.style.color = "red";
        sessionStorage.setItem(`is_liked_${vacation_id}`, 'true');
        updateLikeCount(vacation_id, 1); // Increment like count by 1
    }
    return false;
}


// Validate vacation end date isn't before vacation start date
function validateVacationsDates() {
    const startDateInput = document.getElementsByName("vacation_start_date")[0];
    const endDateInput = document.getElementsByName("vacation_end_date")[0];
    const startDate = new Date(startDateInput.value);
    const endDate = new Date(endDateInput.value);
    
    // Check if end date is before start date
    if (endDate < startDate) {
        endDateInput.setCustomValidity("Vacation start date cannot be after the vacation end date.");
    } else {
        endDateInput.setCustomValidity('');
    }
}

// Validate vacation start date isn't in the past
function validateVacationStartDate() {
    document.getElementById("vacation_start_date").min = new Date().toISOString().split("T")[0];
}