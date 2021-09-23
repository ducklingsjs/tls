<script lang="ts">
	import Header from '$lib/header/Header.svelte';
	import '../app.css';
</script>

<div class="app-container">
	<Header />

	<main>
		<slot />
	</main>

	<footer>
		<p>Made with ♥ by Andreiček and Bambi</p>
	</footer>
</div>

<style>
	footer {
		margin-top: 24px;
		border-top: 1px solid silver;
	}

	p {
		text-align: center;
	}
</style>
