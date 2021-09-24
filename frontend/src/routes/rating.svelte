<script context="module" lang="ts">
	/**
	 * @type {import('@sveltejs/kit').Load}
	 */
	export async function load({ fetch }) {
		const url = 'http://10.1.129.58:5000/api/team';
		const res = await fetch(url);

		if (!res.ok) {
			return {
				status: res.status,
				error: new Error(`Could not load ${url}`)
			};
		}

		return {
			props: {
				teams: await res.json()
			}
		};
	}
</script>

<script lang="ts">
	export let teams: Array<ITeam> = [];

	interface ITeam {
		id: number;
		name: string;
	}

	async function handleSubmit(e): Promise<void> {
		const formData = new FormData(e.target);
		const data = {};

		formData.forEach((value, key) => {
			data[key] = value;
		});

		await fetch('http://10.1.129.58:5000/api/rating', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json; charset=utf-8'
			},
			body: JSON.stringify(data)
		});
	}
</script>

<svelte:head>
	<title>Rating</title>
</svelte:head>

<form on:submit|preventDefault={handleSubmit}>
	<input name="username" placeholder="Username" type="text" />

	<select name="team_id">
		{#each teams as team}
			<option value={team.id}>
				{team.name}
			</option>
		{/each}
	</select>

	<table>
		<tbody>
			<tr>
				<td>App works</td>
				<td><input name="cat_works" type="number" required min="0" max="10" />10</td>
			</tr>
			<tr>
				<td>Technically impressive</td>
				<td><input name="cat_impressive" type="number" required min="0" max="10" />10</td>
			</tr>
			<tr>
				<td>Innovative/Fun</td>
				<td><input name="cat_inovative" type="number" required min="0" max="30" />30</td>
			</tr>
			<tr>
				<td>On topic</td>
				<td><input name="cat_topic" type="number" required min="0" max="10" />10</td>
			</tr>
			<tr>
				<td>Looks</td>
				<td><input name="cat_looks" type="number" required min="0" max="15" />15</td>
			</tr>
			<tr>
				<td>Functionality</td>
				<td><input name="cat_functionality" type="number" required min="0" max="15" />15</td>
			</tr>
			<tr>
				<td>Magic</td>
				<td><input name="cat_magic" type="number" required min="0" max="10" />10</td>
			</tr>
		</tbody>
	</table>

	<button type="submit">Submit</button>
</form>

<style>
</style>
