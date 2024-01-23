<?php
$xml = file_get_contents('https://ghosteshop.com/feed/news.xml');
$games = simplexml_load_string($xml);

$latestGames = [];
foreach ($games->channel->item as $item) {
    $game = [
        'title' => (string)$item->title,
        'pubDate' => (string)$item->pubDate,
        'description' => (string)$item->description,
        'link' => (string)$item->link,
        'image' => (string)$item->comments
    ];
    $latestGames[] = $game;
}

echo json_encode($latestGames);
?>
