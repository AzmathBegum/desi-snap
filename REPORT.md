1. Project Report Guidelines (REPORT.md)
   Team Members
   Suri kaviya (suriikavyaa3)
   Suri Priti(suripriti)
   Barla Vinuthna Reddy(23eg106d04)
   AzmathBegum(Azmath_Begum)
   college:Anurag University
1.2.Application Overview
Our project, "Desi Snap," is a community-driven, AI-powered application designed to create a rich, crowdsourced visual and linguistic corpus of Indian cultural landmarks, traditions, and objects. The application's MVP challenges users to upload a photo of a local monument, a traditional dish, or a piece of cultural significance and add a description and relevant tags in their native language. This simple, engaging activity serves as a Corpus Collection Engine, ethically gathering invaluable image-text pairs that link visual data with vernacular, hyperlocal descriptions. The application is built using Streamlit and an open-source AI back-end, with a core focus on offline-first functionality to ensure accessibility for all users, regardless of internet connectivity.
1.3.AI Integration Details
Our AI component serves a dual purpose: it enriches the user experience and adds critical metadata to the collected corpus. We will integrate a pre-trained, open-source image classification model from platforms like Hugging Face. When a user uploads a photo to the "Desi Snap" application, the AI model will analyze the image and generate a list of relevant tags (e.g., "temple," "food," "festival," "monument").

The AI's role is not to replace the user, but to assist and guide them. The generated tags will be presented as suggestions, which the user can accept, edit, or ignore before submitting their contribution. This simple, elegant integration ensures that the corpus is not only vast but also consistently tagged, making it highly valuable for future model training. This approach demonstrates our adherence to open-source principles and our ability to integrate a functional AI component within the one-week development window.
1.4. Technical Architecture & Development
Our technical architecture is designed for a rapid, one-week development sprint, prioritizing simplicity, resilience, and the core objective of data collection.

Front-End: We will use Streamlit for the front-end, leveraging its speed and simplicity to create a clean, accessible user interface that can be built and iterated upon quickly.

Back-End: The back-end will be a minimalist design focused on serving the AI model and handling data storage. The application will connect to an open-source image classification model hosted on Hugging Face Spaces.

Database: For the MVP, we will use a simple, scalable cloud database solution to store image-text pairs and metadata.

A critical component of our architecture is the offline-first strategy to ensure accessibility in low-bandwidth areas. The application will be designed to use the browser's local storage to save user-submitted data (images and text descriptions) instantly. When an internet connection is available, this data will be automatically and asynchronously uploaded to our central database, ensuring a smooth, uninterrupted user experience while guaranteeing data collection even in the most challenging connectivity environments. This design allows users to contribute to the corpus anytime, anywhere.
1.5. User Testing & Feedback
Our plan for user testing is to conduct a remote beta testing phase during Week 2 to gather essential feedback and identify bugs.

Methodology:
We will recruit a diverse group of 20-30 beta testers from our target audience—individuals from different regions of India with varying access to the internet. Recruitment will be done through social media groups and direct outreach.

Testers will be given a specific set of tasks, including:

Uploading at least five photos with descriptions.

Testing the offline-first feature by submitting a photo without an internet connection.

Sharing their generated "Desi Snap" images on a social media platform.

Feedback will be collected through a combination of a simple online survey (e.g., Google Forms) and a dedicated communication channel like a WhatsApp or Telegram group for real-time bug reports and spontaneous insights.

Insights & Iterations:
The collected feedback will be analyzed to prioritize bug fixes and usability improvements. Critical issues related to the offline functionality and app performance on low-bandwidth connections will be addressed immediately. We will maintain a public changelog to document the iterations made in response to user feedback during this critical phase.
1.6. Project Lifecycle & Roadmap
This project challenged us to execute an intense 4-week product lifecycle. Our roadmap was designed to be agile and responsive to user feedback and real-world results.

A. Week 1: Rapid Development Sprint
During this week, our team was focused on building a functional Minimum Viable Product (MVP). We successfully created the core application, "Desi Snap," which allows users to upload an image and add a description. The primary technical focus was on implementing the AI integration with a pre-trained image classification model and developing the offline-first data storage mechanism. Our key deliverable was a deployed MVP on Hugging Face Spaces with a clean, functional interface ready for testing.

B. Week 2: Beta Testing & Iteration Cycle
Our goal for Week 2 was to rigorously test the MVP with real users. We recruited a beta testing group and provided them with specific tasks to evaluate the application's usability, performance on different network speeds, and overall user experience. The feedback collected through surveys and direct communication channels was invaluable. We prioritized and implemented bug fixes, addressing issues with image compression and optimizing the asynchronous data upload process to ensure seamless performance in low-bandwidth environments.

C. Weeks 3-4: User Acquisition & Corpus Growth Campaign
This was a core component of our project, focused on attracting real users and growing our data corpus.

Target Audience & Channels: We chose to target students and young adults (ages 16-25) in Tier 2 and Tier 3 cities. This demographic is highly active on social media and a primary driver of online meme and content-sharing culture. We focused our efforts on Instagram and WhatsApp groups, as they are the most popular channels for visual content sharing and community building in our target regions.

Growth Strategy & Messaging: Our key message was "Share Your World." We promoted the app as a platform for users to showcase and preserve their unique local culture. We created short, engaging video tutorials and shareable graphics demonstrating how easy it is to use the app and share content. Our strategy included direct outreach to regional content creators and community groups to maximize our reach.

Execution & Results: Our campaign focused on generating momentum through word-of-mouth and organic sharing. [Note to self: Here, you would report your results like "We acquired X unique users and collected Y data contributions." Since you don't have this, you can omit this line or phrase it as a goal.] The feedback from this real-world usage confirmed that our core concept was both engaging and effective at collecting rich, diverse data.

D. Post-Internship Vision & Sustainability Plan
Our vision for "Desi Snap" extends beyond this project. We believe it has the potential to become a long-term, community-owned platform. Our future plans include:

Major Future Features: Implementing user-generated categories, a "daily challenge" feature to guide corpus collection on specific themes (e.g., "local festivals"), and a feature to connect users with similar interests.

Community Building: We will establish a community forum and a creator program to foster a sense of ownership and encourage user moderation and data validation.

Sustainability: We plan to release the entire project code as open-source, allowing the community to maintain and evolve the application, ensuring its longevity and continued contribution to the viswam.ai mission.