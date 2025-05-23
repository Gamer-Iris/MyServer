INSERT INTO roles (role, role_details, login_text, logout_text, kick_text, ban_text, update_time) VALUES
(0, 'プレイヤー',
    '【プレイヤー】%s さんがログインしました。',
    '【プレイヤー】%s さんがログアウトしました。',
    '【プレイヤー】%s さんがキックされました。',
    '【プレイヤー】%s さんがBANされました。',
    NOW()),
(1, 'モデレーター',
    '【モデレーター】%s さんがログインしました。',
    '【モデレーター】%s さんがログアウトしました。',
    '【モデレーター】%s さんが秩序維持のために一時退場となりました。（キック）',
    '【モデレーター】%s さんが規約違反により追放されました。（BAN）',
    NOW()),

(2, 'ゲームマスター',
    '【ゲームマスター】%s さんが異世界より現れました。（ログイン）',
    '【ゲームマスター】%s さんが次元の扉をくぐり去っていきました。（ログアウト）',
    '【ゲームマスター】%s さんが神の意志により退場となりました。（キック）',
    '【ゲームマスター】%s さんが禁忌を犯したため、封印されました。（BAN）',
    NOW()),

(3, '管理者',
    '【管理者】%s さんが天空から舞い降りました。（ログイン）',
    '【管理者】%s さんが静かに姿を消しました。（ログアウト）',
    '【管理者】%s さんが鉄槌を下され、一時離脱となりました。（キック）',
    '【管理者】%s さんが世界の理から外されました。（BAN）',
    NOW()),

(4, 'サーバー所有者',
    '【サーバー所有者】%s さんが召喚されました！世界がその登場に震えます！（ログイン）',
    '【サーバー所有者】%s さんが次なる創造の地へと旅立ちました。（ログアウト）',
    '【サーバー所有者】%s さんが神の判断により一時追放されました。（キック）',
    '【サーバー所有者】%s さんが運命の裁きによりBANされました。（BAN）',
    NOW());
