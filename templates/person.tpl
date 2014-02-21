{{ person.personality }} {{ person.age }}-year-old {{ person.genderPronoun }} has {{ person.eyecolor }} eyes, a {{ person.skincolor }} complexion, and {{ person.hairtype }} {{ person.haircolor }} hair {{ person.hairstyle }}.
{{ person.genderTitle.capitalize() }} is {{ person.height }} and {{ person.build }}. {{ person.genderTitle.capitalize() }} is from  {{ person.birthPlace }}.
% if person.previousService:
    {{ person.rank.title }} {{ person.lastName }} previously served aboard the {{ prefix }} {{ person.previousService }}.
% end