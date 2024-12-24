<template>
  <project-card
    :title="title"
    :id="id"
    :titleImage="titleImage"
    :summary="summary"
    :date="date"
  >
    <blog-paragraph>
      Maecenas enim tortor, porttitor vel varius id, aliquam non ipsum. Aliquam tincidunt velit ligula, sed luctus felis dignissim ullamcorper. Nunc dolor ex, ultricies non pharetra vel, varius eu elit. Nullam quis mi vel velit hendrerit elementum. Sed semper, augue ut congue rutrum, nibh velit imperdiet ligula, nec convallis urna velit id sem. Donec congue ipsum sed sapien lacinia, id ornare augue fringilla. Curabitur venenatis eros quis elementum bibendum. Nam sodales porta varius. Curabitur tristique, massa eu dapibus semper, lacus lacus volutpat turpis, eget lacinia nibh arcu in odio. Praesent laoreet eu felis nec cursus.
    </blog-paragraph>

    <blog-paragraph>
      Cras ut venenatis arcu. Nullam viverra, enim eu tincidunt mollis, quam sem consequat risus, non pretium purus magna porttitor sem. Proin fringilla urna eget tincidunt venenatis. Cras et dapibus erat. Vestibulum mattis eget nunc vitae feugiat. Phasellus quis hendrerit elit. Nullam nec neque in augue pulvinar sollicitudin. Suspendisse vel felis maximus, iaculis lacus vel, faucibus augue. Nulla volutpat eu urna nec rutrum. Etiam ipsum ante, mattis fermentum tincidunt tempus, vulputate faucibus elit. Suspendisse luctus vitae diam ac vestibulum. Cras ullamcorper massa in ipsum hendrerit convallis. Sed nec pulvinar mi.
    </blog-paragraph>
  </project-card>
</template>

<script>
import ProjectCard from '@/components/projects/ProjectCard.vue'
  export default {
  components: { ProjectCard },
    data: () => ({
      title: 'Übersetzung mit HHU',
      id: 'hhu',
      titleImage: '/images/projects/hhu_logo_cropped.jpeg',
      summary: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus id cursus elit. Aenean aliquam, ante vitae venenatis facilisis, lorem ipsum sollicitudin orci, et auctor libero urna sed erat.',
      date: new Date(2024, 8, 1)
    }),
  }
</script>