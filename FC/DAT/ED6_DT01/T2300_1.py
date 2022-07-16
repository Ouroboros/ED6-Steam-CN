import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2300_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2300_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T2300.x'
    header.mapIndex       = 1
    header.bgm            = 15
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1234
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
    )

# id: 0x10001 offset: 0x64
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10002 offset: 0x64
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0x64
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x64
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x64
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x64
@scena.Code('PreInit')
def PreInit():
    EventBegin(0x00)
    ClearMapFlags(0x00000001)
    Fade(1000)
    OP_6C(338000, 0)
    SetChrPos(0x0000, -3200, 8000, 44000, 315)
    SetChrPos(0x0001, -2000, 8000, 43900, 315)
    SetChrPos(0x0002, -2800, 8000, 42500, 315)
    OP_69(0x0000, 2000)
    TalkBegin(0x000E)
    OP_4A(0x00FE, 255)
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '#1740160522V………………啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1740160523V请问……\n',
            '你们是游击士协会的人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x001F, 0x00, 0x02)"),
            Expr.Return,
        ),
        'loc_35F',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_195',
    )

    ChrTalk(
        0x0101,
        (
            '#0010150861V#501F…………嗯？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160525V#000F嗯，正是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160526V难不成，\n',
            '你就是阿梅莉娅小姐吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_285')

    def _loc_195(): pass

    label('loc_195')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1E4',
    )

    ChrTalk(
        0x0102,
        (
            '#0020160527V#014F嗯，是的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160528V您就是阿梅莉娅小姐吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_285')

    def _loc_1E4(): pass

    label('loc_1E4')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_285',
    )

    ChrTalk(
        0x0105,
        (
            '#0060160529V#044F啊，是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060160530V虽然我不是，\n',
            '不过这两位确实是游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x00FE, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160531V#000F哎，难道……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160532V你就是阿梅莉娅小姐吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    def _loc_285(): pass

    label('loc_285')

    ChrTalk(
        0x00FE,
        (
            '#1740160533V啊，我就是。\n',
            '终于等到你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x00FE, 400)

    ChrTalk(
        0x0102,
        (
            '#0020160534V#010F那就开门见山吧，\n',
            '您的委托内容是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160535V护送的任务吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#1740160536V嗯，是的。\n',
            '希望你们能够护送我叔父。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1740160537V因为他要去古罗尼山道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4E5')

    def _loc_35F(): pass

    label('loc_35F')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3BE',
    )

    ChrTalk(
        0x0101,
        (
            '#0010160576V#004F哎？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160577V嗯，然后呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x00FE, 400)

    ChrTalk(
        0x0102,
        (
            '#0020160578V#010F有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_480')

    def _loc_3BE(): pass

    label('loc_3BE')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_405',
    )

    ChrTalk(
        0x0102,
        (
            '#0020160527V#014F嗯，是的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160578V#010F有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_480')

    def _loc_405(): pass

    label('loc_405')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_480',
    )

    ChrTalk(
        0x0105,
        (
            '#0060160529V#044F啊，是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060160530V虽然我不是，\n',
            '不过这两位确实是游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x00FE, 400)

    ChrTalk(
        0x0102,
        (
            '#0020160578V#010F有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_480(): pass

    label('loc_480')

    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#1740160584V嗯，其实……\n',
            '希望你们能够护送我叔父。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1740160585V因为他要去\n',
            '古罗尼山道办点事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_4E5(): pass

    label('loc_4E5')

    ChrTurnDirection(0x0101, 0x00FE, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160538V#000F古罗尼山道啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160539V#508F那么，\n',
            '最终目的地是柏斯吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1740160540V不，不是这样的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1740160541V他只是单纯地\n',
            '想到古罗尼山道去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160542V#004F咦？为什么？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160543V去古罗尼山道……\n',
            '能有什么事做呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1740160544V唔……\n',
            '他说是去寻找珍稀的野菜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1740160545V对不起，\n',
            '我也不太明白\n',
            '叔父所说的意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010160546V#007F哦…………\n',
            '是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x00FE, 400)

    ChrTalk(
        0x0102,
        (
            '#0020160547V#010F那么就向他本人询问一下，\n',
            '这样更直接。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#1740160548V嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0000, 400)

    ChrTalk(
        0x00FE,
        (
            '#1740160549V请稍等片刻。\n',
            '我这就去叫他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x00FE, -5600, 8500, 47000, 3000, 0x00)
    SetChrDirection(0x00FE, 270, 0)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 30)
    OP_73(0x0000)
    SetChrFlags(0x00FE, 0x0040)
    OP_94(0x01, 0x00FE, 0x0000, 0x000009C4, 0x00000BB8, 0x00)
    OP_72(0x0000, 0x0800)
    PlaySE(7, 0x00, 0x64)
    OP_6F(0x0000, 30)
    OP_70(0x0000, 0)
    OP_73(0x0000)
    OP_71(0x0000, 0x0800)
    SetChrFlags(0x00FE, 0x0008)

    If(
        (
            (Expr.Eval, "OP_29(0x001F, 0x00, 0x02)"),
            Expr.Return,
        ),
        'loc_7E4',
    )

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160550V#003F看到公告板的时候，\n',
            '我还以为这次任务比较简单……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160551V为什么突然感觉\n',
            '事情变得这么怪了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_810')

    def _loc_7E4(): pass

    label('loc_7E4')

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160552V#505F嗯～\n',
            '真是不明白呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_810(): pass

    label('loc_810')

    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060160553V#043F古罗尼山道是一个相当危险的地方。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060160554V那样的地方，\n',
            '为何还要专程前去呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0105, 400)

    ChrTalk(
        0x0102,
        (
            '#0020160555V#010F是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160556V总之还是向他本人\n',
            '问清楚这件事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    SetChrDirection(0x0101, 315, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160557V#000F……啊，好像来了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0906')
    def lambda_0906():
        SetChrDirection(0x0102, 315, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0906)

    @scena.Lambda('lambda_0914')
    def lambda_0914():
        SetChrDirection(0x0105, 315, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_0914)

    ClearChrFlags(0x00FE, 0x0008)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 30)
    OP_73(0x0000)
    SetChrDirection(0x00FE, 90, 0)
    OP_94(0x01, 0x00FE, 0x0000, 0x000009C4, 0x00000BB8, 0x00)
    SetChrDirection(0x00FE, 270, 400)
    OP_72(0x0000, 0x0800)
    PlaySE(7, 0x00, 0x64)
    OP_6F(0x0000, 30)
    OP_70(0x0000, 0)
    OP_73(0x0000)
    OP_71(0x0000, 0x0800)
    ChrWalkTo(0x00FE, -4100, 8000, 45100, 3000, 0x00)
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    ChrTurnDirection(0x0101, 0x00FE, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160558V#000F咦？\n',
            '您的叔父呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1740160559V是这样的………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1740160560V他好像\n',
            '早就已经出发了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010160561V#004F啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x00FE, 400)

    ChrTalk(
        0x0102,
        (
            '#0020160562V#014F出发了…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160563V去了古罗尼山道……是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#1740160564V嗯，应该是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x00FE, 0, 400)

    ChrTalk(
        0x00FE,
        (
            '#1740160565V我告诉过他\n',
            '要等你们一起的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1740160566V叔父真是的，\n',
            '实在是太乱来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160567V#003F嗯，真让人担心啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160568V竟然一个人就跑到\n',
            '古罗尼山道去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160569V#013F更何况现在天色越来越暗，\n',
            '一个人实在很危险啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160570V希望他能在天黑之前\n',
            '赶回来就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1740160571V唉…………\n',
            '对不起啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1740160572V让你们专程赶来，\n',
            '结果却白跑了一趟……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010160573V#000F没什么，不用介意。\n',
            '对我们来说这没关系的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1740160574V真的很抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1740160575V等叔父回来之后，\n',
            '我会好好和他谈谈的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x001F, 0x04, 0x04)
    OP_28(0x001F, 0x04, 0x02)
    OP_28(0x001F, 0x01, 0x0001)
    OP_28(0x001F, 0x01, 0x0002)
    OP_28(0x001F, 0x01, 0x0004)
    ChrWalkTo(0x00FE, -5600, 8500, 47000, 3000, 0x00)
    SetChrDirection(0x00FE, 270, 0)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 30)
    OP_73(0x0000)
    SetChrFlags(0x00FE, 0x0040)
    OP_94(0x01, 0x00FE, 0x0000, 0x000009C4, 0x00000BB8, 0x00)
    OP_72(0x0000, 0x0800)
    PlaySE(7, 0x00, 0x64)
    OP_6F(0x0000, 30)
    OP_70(0x0000, 0)
    OP_73(0x0000)
    OP_71(0x0000, 0x0800)
    SetChrFlags(0x00FE, 0x0008)
    SetChrFlags(0x00FE, 0x0080)
    OP_4B(0x00FE, 255)
    EventEnd(0x00)
    TalkEnd(0x000E)

    Return()

# id: 0x0001 offset: 0xD63
@scena.Code('Init')
def Init():
    FadeIn(2000, 0)
    EventBegin(0x00)
    ClearMapFlags(0x00000001)
    SetMapFlags(0x00400000)
    OP_6C(270000, 0)
    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0010, -2780, 8000, 59500, 180)
    SetChrPos(0x0101, -1780, 8000, 61500, 180)
    SetChrPos(0x0102, -3780, 8000, 62500, 180)
    SetChrPos(0x0105, -2780, 8000, 63500, 180)
    CameraMove(-2750, 7990, 58240, 0)

    @scena.Lambda('lambda_0DE1')
    def lambda_0DE1():
        OP_6C(315000, 5000)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_0DE1)

    @scena.Lambda('lambda_0DF1')
    def lambda_0DF1():
        OP_94(0x01, 0x0010, 0x0000, 0x00001CE8, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_0DF1)

    Sleep(100)

    @scena.Lambda('lambda_0E0C')
    def lambda_0E0C():
        OP_94(0x01, 0x0101, 0x0000, 0x00002008, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0E0C)

    Sleep(50)

    @scena.Lambda('lambda_0E27')
    def lambda_0E27():
        OP_94(0x01, 0x0102, 0x0000, 0x00002260, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0E27)

    Sleep(50)

    @scena.Lambda('lambda_0E42')
    def lambda_0E42():
        OP_94(0x01, 0x0105, 0x0000, 0x000021FC, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_0E42)

    OP_0D()
    CameraMove(-2840, 7990, 52900, 4000)
    WaitForThreadExit(0x0010, 0x0001)
    ChrTurnDirection(0x0010, 0x0105, 400)
    Sleep(800)

    ChrTalk(
        0x0010,
        (
            '#1070160722V唔，到这里就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1070160723V今天真是\n',
            '承蒙你们的照顾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0005, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_10F0',
    )

    ChrTurnDirection(0x0010, 0x0101, 400)

    ChrTalk(
        0x0010,
        (
            '#1070160724V这样吧。\n',
            '借此难得的机会，\n',
            '以前的不愉快也都一笔勾销如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1070160725V怎么说我和你们\n',
            '都还算有些缘分啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1070160726V如果可以的话，\n',
            '今后我们\n',
            '还是做朋友吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0F7B')
    def lambda_0F7B():
        ChrTurnDirection(0x0105, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_0F7B)

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020160727V#010F这样也好……\n',
            '艾丝蒂尔你觉得呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0010, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160728V#505F唔…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160729V既然奥维德先生都这么说了，\n',
            '那我当然也没问题……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_101F')
    def lambda_101F():
        ChrTurnDirection(0x0105, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_101F)

    ChrTurnDirection(0x0102, 0x0010, 400)

    ChrTalk(
        0x0102,
        (
            '#0020160730V#019F和解成功……了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160731V#010F那么从现在开始大家就是朋友了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0102, 400)

    ChrTalk(
        0x0010,
        (
            '#1070160732V嗯，听你这么一说，\n',
            '我也感到很高兴啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0105, 400)

    ChrTalk(
        0x0010,
        (
            '#1070160733V那我们就在\n',
            '下次的工作中再会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1177')

    def _loc_10F0(): pass

    label('loc_10F0')

    ChrTurnDirection(0x0101, 0x0010, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160734V#508F嗯，工作请加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0010, 400)

    ChrTalk(
        0x0102,
        (
            '#0020160735V#010F那么，\n',
            '我们告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1070160736V唔，再见。\n',
            '就在下次的工作中再会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1177(): pass

    label('loc_1177')

    SetChrDirection(0x0010, 180, 400)
    SetChrFlags(0x0010, 0x0040)

    @scena.Lambda('lambda_1189')
    def lambda_1189():
        ChrTurnDirection(0x0101, 0x0010, 0)
        Yield()

        Jump('lambda_1189')

    DispatchAsync2(0x0101, 0x0001, lambda_1189)

    @scena.Lambda('lambda_119A')
    def lambda_119A():
        ChrTurnDirection(0x0102, 0x0010, 0)
        Yield()

        Jump('lambda_119A')

    DispatchAsync2(0x0102, 0x0001, lambda_119A)

    @scena.Lambda('lambda_11AB')
    def lambda_11AB():
        ChrTurnDirection(0x0105, 0x0010, 0)
        Yield()

        Jump('lambda_11AB')

    DispatchAsync2(0x0105, 0x0001, lambda_11AB)

    OP_94(0x01, 0x0010, 0x0000, 0x00002328, 0x00000BB8, 0x00)
    SetChrFlags(0x0010, 0x0080)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x0105, 0x01)
    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【护送上山的叔父】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    ClearMapFlags(0x00400000)
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
