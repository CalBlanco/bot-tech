from annot_ui import TextAnnotator

annotator = TextAnnotator({"labels": {"label_type": ["option1", "option2", "option3"]}})
annotator.run()