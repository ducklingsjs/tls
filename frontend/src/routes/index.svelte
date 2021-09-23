<script context="module" lang="ts">
	import hacker from './../../static/hacker.gif';

	export const prerender = true;
</script>

<svelte:head>
	<title>Home</title>
</svelte:head>

<section>
	<img src={hacker} alt="SvelteKit" />
</section>

<style>
	section {
		display: flex;
		align-items: center;
		justify-content: center;
	}
</style>
