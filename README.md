# ArguGraph
Structural reasoning reconstruction demo 
ArguGraph is an AI-assisted system for reconstructing and visualizing the argumentative structure of student essays. Rather than evaluating writing based on surface features such as length, vocabulary, or grammatical correctness, ArguGraph models how ideas are organized, connected, and justified in argument writing.

Each essay is manually segmented into independent propositions and annotated with hierarchical relations to form a gold-standard structure. We fine-tune a transformer encoder to predict parent–child attachments between propositions. During inference, candidate parents are ranked for each proposition, and the highest-scoring attachment is selected to reconstruct an argument tree.

We compare two structural representations: a Collapsed model, which restricts attachment to observable segments, and an Expanded model, which preserves abstract coordination nodes. Results show that Collapsed structures work better on simpler essays, whereas Expanded representations better capture deep coordination in complex essays.

A live demo of ArguGraph is available at https://argugraphers.streamlit.app/. This interactive app allows users to select essays, view both the human-annotated reference structure and model-generated structures, and compare structural metrics such as maximum depth, width, and ranking accuracy. The app makes argument structure visible and interpretable, supporting educators and researchers in diagnosing student reasoning.

ArguGraph demonstrates that transformer-based models can approximate human-annotated argument structure and opens a pathway toward scalable structural diagnostics in writing assessment.
