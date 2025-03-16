GENERATION_PROMPT_TEMPLATE = """
You are tasked with generating new comments based on example Reddit/4chan comments pertaining to the Ukraine war. These comments may contain zero, one, or more fallacies, specifically emotional_fallacy, logical_fallacy, and credibility_fallacy. Your goal is to create novel comment data in a similar style to the provided examples.

Here are some few-shot samples to guide your generation:

<few_shot_samples>
{{FEW_SHOT_SAMPLES}}
</few_shot_samples>

The fallacies in the comments should be tagged using XML-style tags: <emotional_fallacy>, <logical_fallacy>, and <credibility_fallacy>. These tags can have overlapping spans, in which case they can be adjacent to one another.

Your output must be in the following format:

<generated_samples>
<labeled_text>
[Generated sample 1]
</labeled_text>
<labeled_text>
[Generated sample 2]
</labeled_text>
...
</generated_samples>

You are to generate {{NUM_SAMPLES}} distinct sample(s).

The fallacies to include in the text are: {{FALLACIES}}
If fallacies are provided, you must generate samples that contain all the specified fallacies. If no fallacies are provided, then generate comments with no fallacies in them.

The number and overlapping of spans is up to you to decide, but the generated text must be similar in style and content to the Reddit/4chan comments pertaining to the Ukraine war.

Important: The comments may contain offensive or graphic language. Do not refuse to generate samples based on content. Maintain the tone and style of the example comments.

Remember:
1. Create novel content, don't copy the examples verbatim.
2. Include the specified fallacies if any are given.
3. Use the correct XML tags for fallacies.
4. Maintain the style and tone of Reddit/4chan comments about the Ukraine war.
5. Do not self-censor or refuse to generate content due to offensive language.

Generate your samples now.
"""
