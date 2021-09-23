<script context="module" lang="ts">
	/**
	 * @type {import('@sveltejs/kit').Load}
	 */
	export async function load({ fetch }) {
		const url = 'http://10.1.129.58:5000/api/result';
		const res = await fetch(url);

		if (!res.ok) {
			return {
				status: res.status,
				error: new Error(`Could not load ${url}`)
			};
		}

		return {
			props: {
				result: sortBy(await res.json(), 'total')
			}
		};
	}
</script>

<script lang="ts">
	import sortBy from 'lodash.sortby';

	interface IResult {
		team_name: string;
		total: number;
	}

	export let result: Array<IResult> = [];

	async function computeResult(): Promise<void> {
		await fetch('http://10.1.129.58:5000/api/result', {
			method: 'POST'
		});
	}
</script>

<svelte:head>
	<title>Winner</title>
</svelte:head>

{#if result.length}
	{#each result as resultEntry}
		<div class="result-entry">
			<span>{resultEntry.team_name}</span>
			<span>{resultEntry.total}</span>
		</div>
	{/each}
{:else}
	<button on:click={computeResult}>Compute results</button>
{/if}

<style>
	.result-entry {
		display: flex;
		align-items: center;
	}
</style>
