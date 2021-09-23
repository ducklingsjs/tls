<script lang="ts">
	import { page } from '$app/stores';
</script>

<header>
	<nav>
		<ul>
			<li class:active={$page.path === '/'}><a sveltekit:prefetch href="/">Home</a></li>
			<li class:active={$page.path === '/rating'}><a sveltekit:prefetch href="/rating">Rating</a></li>
			<li class:active={$page.path === '/winners'}><a sveltekit:prefetch href="/winners">Winners</a></li>
		</ul>
	</nav>
</header>

<style>
	header {
		margin-bottom: 24px;
		border-bottom: 1px solid silver;
	}

	nav {
		padding: 24px;
	}

	ul {
		display: flex;
		align-items: center;
		justify-content: center;
		gap: 16px;
		margin: 0;
		padding: 0;
		list-style: none;
	}
</style>
