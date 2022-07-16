import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2521_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2521_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T2600.x'
    header.mapIndex       = 1
    header.bgm            = 31
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x10A0
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
    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x1000)"),
            Expr.Return,
        ),
        'loc_134',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E7',
    )

    TalkBegin(0x0015)
    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x00FE,
        (
            '多亏你们，\n',
            '我终于集齐了全部三本必要的资料。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好了，\n',
            '那么我就继续展开研究了，\n',
            '时间已经不多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_131')

    def _loc_E7(): pass

    label('loc_E7')

    SetChrFlags(0x0015, 0x0010)
    TalkBegin(0x0015)

    ChrTalk(
        0x00FE,
        (
            '唔～原来如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们的预测\n',
            '还有可以修正的余地啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x0015, 0x0010)

    def _loc_131(): pass

    label('loc_131')

    Jump('loc_A8A')

    def _loc_134(): pass

    label('loc_134')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_19F',
    )

    TalkBegin(0x0015)

    ChrTalk(
        0x00FE,
        (
            '#1930171191V如果找到了《卢安经济史》，\n',
            '请务必告诉我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1930171192V为了学园祭，\n',
            '就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A8A')

    def _loc_19F(): pass

    label('loc_19F')

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0200)"),
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0400)"),
            Expr.Or,
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0800)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_42E',
    )

    TalkBegin(0x0015)
    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '#1930171193V呼，\n',
            '作为研究根据的资料还不太够啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1930171194V其余的《卢安经济史》\n',
            '你们在哪里看到过吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_40(0x033D)"),
            (Expr.Eval, "OP_40(0x033E)"),
            Expr.Or,
            (Expr.Eval, "OP_40(0x033F)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_397',
    )

    EventBegin(0x00)

    ChrTalk(
        0x0101,
        (
            '#0010171195V#006F嘿嘿～已经找到了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_40(0x033D)"),
            Expr.Return,
        ),
        'loc_2BA',
    )

    RemoveItem(0x033D, 1)
    OP_28(0x0027, 0x01, 0x0200)
    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '卢安经济史·上',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    def _loc_2BA(): pass

    label('loc_2BA')

    If(
        (
            (Expr.Eval, "OP_40(0x033E)"),
            Expr.Return,
        ),
        'loc_312',
    )

    RemoveItem(0x033E, 1)
    OP_28(0x0027, 0x01, 0x0400)
    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '卢安经济史·中',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    def _loc_312(): pass

    label('loc_312')

    If(
        (
            (Expr.Eval, "OP_40(0x033F)"),
            Expr.Return,
        ),
        'loc_36A',
    )

    RemoveItem(0x033F, 1)
    OP_28(0x0027, 0x01, 0x0800)
    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '卢安经济史·下',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    def _loc_36A(): pass

    label('loc_36A')

    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1930171196V哦，我就在等它呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x0001)

    Jump('loc_42B')

    def _loc_397(): pass

    label('loc_397')

    ChrTalk(
        0x0101,
        (
            '#0010171197V#003F唔～\n',
            '好像没有看见过呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060171198V#040F嗯，是啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1930171199V哦，是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1930171200V如果看到了其余的书，\n',
            '还请过来告诉我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_42B(): pass

    label('loc_42B')

    Jump('loc_A8A')

    def _loc_42E(): pass

    label('loc_42E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_4F4',
    )

    TalkBegin(0x0015)

    ChrTalk(
        0x00FE,
        (
            '#1930171201V因为是用于研究成果展示的资料，\n',
            '所以无论如何也要找到……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1930171202V是名为《卢安经济史》的\n',
            '三本一套的老书，\n',
            '不知道被谁给拿走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1930171188V如果找到了的话，\n',
            '请务必告诉我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A8A')

    def _loc_4F4(): pass

    label('loc_4F4')

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0020)"),
            Expr.Return,
        ),
        'loc_7EA',
    )

    TalkBegin(0x0015)
    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '#1930171193V呼，\n',
            '作为研究根据的资料还不太够啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1930171205V《卢安经济史》这套书\n',
            '你们在哪里看到过吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_40(0x033D)"),
            (Expr.Eval, "OP_40(0x033E)"),
            Expr.Or,
            (Expr.Eval, "OP_40(0x033F)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_742',
    )

    EventBegin(0x00)

    ChrTalk(
        0x0101,
        (
            '#0010171206V#000F嗯～你说的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010171207V应该就是这本书了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060160921V#040F嗯，我想也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060171209V罗基克，\n',
            '你要找的是这本书吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_40(0x033D)"),
            Expr.Return,
        ),
        'loc_65C',
    )

    RemoveItem(0x033D, 1)
    OP_28(0x0027, 0x01, 0x0200)
    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '卢安经济史·上',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    def _loc_65C(): pass

    label('loc_65C')

    If(
        (
            (Expr.Eval, "OP_40(0x033E)"),
            Expr.Return,
        ),
        'loc_6B4',
    )

    RemoveItem(0x033E, 1)
    OP_28(0x0027, 0x01, 0x0400)
    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '卢安经济史·中',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    def _loc_6B4(): pass

    label('loc_6B4')

    If(
        (
            (Expr.Eval, "OP_40(0x033F)"),
            Expr.Return,
        ),
        'loc_70C',
    )

    RemoveItem(0x033F, 1)
    OP_28(0x0027, 0x01, 0x0800)
    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '卢安经济史·下',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    def _loc_70C(): pass

    label('loc_70C')

    ChrTurnDirection(0x00FE, 0x0105, 400)

    ChrTalk(
        0x00FE,
        (
            '#1930171210V哦，没错。\n',
            '我要找的就是它。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x0001)

    Jump('loc_7E7')

    def _loc_742(): pass

    label('loc_742')

    ChrTalk(
        0x0101,
        (
            '#0010171211V#002F唔～\n',
            '好像没有看见过呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060171212V#040F抱歉，罗基克。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1930171213V哎呀～又不是你们的错，\n',
            '不用道歉啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1930171214V如果看到的话，\n',
            '还请过来告诉我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_7E7(): pass

    label('loc_7E7')

    Jump('loc_A8A')

    def _loc_7EA(): pass

    label('loc_7EA')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))
    OP_28(0x0027, 0x01, 0x0020)
    ClearChrFlags(0x0015, 0x0010)
    TalkBegin(0x0015)
    EventBegin(0x00)
    ChrTurnDirection(0x0015, 0x0105, 0)
    OP_4A(0x0015, 255)

    ChrTalk(
        0x00FE,
        (
            '#1930171177V唔，是科洛丝啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060171178V#044F啊，罗基克。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060171179V你还在做成果展览的资料收集吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1930171180V嗯，是啊。\n',
            '再加把劲就可以了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1930171181V但是作为研究最终根据的\n',
            '必要资料还没有找到呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060171182V#043F啊……\n',
            '这可就麻烦了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1930171183V是名为《卢安经济史》的\n',
            '三本一套的老书。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1930171184V资料室里没有，\n',
            '应该是被人拿出去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1930171185V你们有没有在学院里\n',
            '看到过那几本书呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010171186V#003F唔……\n',
            '没有注意到哪里有呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1930171187V这样啊……不过，\n',
            '肯定是在校园的某个地方的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0105, 400)

    ChrTalk(
        0x00FE,
        (
            '#1930171188V如果找到了的话，\n',
            '请务必告诉我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060171189V#040F嗯，我知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060171190V如果找到了，\n',
            '我们会立刻来告诉你的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x0015, 0x0010)
    EventEnd(0x01)
    OP_4B(0x0015, 255)

    def _loc_A8A(): pass

    label('loc_A8A')

    TalkEnd(0x0015)

    Return()

# id: 0x0001 offset: 0xA8E
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0200)"),
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0400)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0800)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_D1B',
    )

    OP_28(0x0027, 0x01, 0x1000)
    OP_28(0x003D, 0x01, 0x0400)
    OP_2C(0x003D, 0x01F4)
    OP_2B(0x003D, 0x0001)

    ChrTalk(
        0x00FE,
        (
            '#1930171220V好，这样一来，\n',
            '三本必要的资料终于都到手了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x00FE, 400)

    ChrTalk(
        0x0105,
        (
            '#0060171221V#040F呵呵，罗基克，\n',
            '我期待着你的研究成果哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0105, 400)

    ChrTalk(
        0x00FE,
        (
            '#1930171222V嗯，敬请期待。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1930171223V能够得到科洛丝你们\n',
            '这样尽力的帮助，\n',
            '我一定会做到最好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1930171224V好了，\n',
            '那么我就继续展开研究了，\n',
            '时间已经不多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1930171225V科洛丝你们的\n',
            '舞台剧也要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060171226V#040F嗯，我们是不会被比下去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060171227V#040F……是吧，艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x00FE, 400)

    ChrTalk(
        0x0101,
        (
            '#0010171228V#001F嘿嘿，你就好好期待吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1930171229V嗯，我们一起加油吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '学园祭的校园任务\n',
            '【收集研究资料】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    WaitEffect(0x02, 0x03)
    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    Sleep(100)

    Jump('loc_E2C')

    def _loc_D1B(): pass

    label('loc_D1B')

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0200)"),
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0400)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0200)"),
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0800)"),
            Expr.Nez64,
            Expr.Or,
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0400)"),
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0800)"),
            Expr.Nez64,
            Expr.Or,
            Expr.Return,
        ),
        'loc_DA3',
    )

    ChrTalk(
        0x00FE,
        (
            '#1930171218V最后一本肯定\n',
            '也在学院里面的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1930171192V为了学园祭，\n',
            '就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E2C')

    def _loc_DA3(): pass

    label('loc_DA3')

    ChrTalk(
        0x00FE,
        (
            '#1930171215V应该还有\n',
            '另外两本的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1930171216V有了这上面的资料，\n',
            '我的研究成果展览\n',
            '就会很充实了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1930171192V为了学园祭，\n',
            '就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E2C(): pass

    label('loc_E2C')

    EventEnd(0x01)
    TalkEnd(0x0015)

    Return()

# id: 0x0002 offset: 0xE32
@scena.Code('ReInit')
def ReInit():
    ClearScenaFlags(ScenaFlag(0x0001, 2, 0xA))
    ClearScenaFlags(ScenaFlag(0x0001, 3, 0xB))
    PlaySE(17, 0x00, 0x64)
    SetChrFlags(0x0016, 0x0080)
    OP_64(0x01, 0x0001)
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '卢安经济史·上',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(0x033D, 1)
    OP_28(0x0027, 0x01, 0x0040)
    TalkEnd(0x00FF)

    Return()

# id: 0x0003 offset: 0xE9E
@scena.Code('func_03_E9E')
def func_03_E9E():
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '书架大部分地方都空着。\n',
            '看起来资料都被拿走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    If(
        (
            (Expr.Eval, "OP_40(0x033D)"),
            (Expr.Eval, "OP_40(0x033E)"),
            Expr.Or,
            (Expr.Eval, "OP_40(0x033F)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1075',
    )

    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        10,
        0,
        (
            TXT(0x00, '【归还卢安经济史】\n'),
            TXT(0x01, '【不归还】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_F67'),
        (0x00000001, 'loc_1072'),
        (-1, 'loc_1075'),
    )

    def _loc_F67(): pass

    label('loc_F67')

    If(
        (
            (Expr.Eval, "OP_40(0x033D)"),
            Expr.Return,
        ),
        'loc_FBF',
    )

    RemoveItem(0x033D, 1)
    OP_28(0x0027, 0x01, 0x0200)
    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '归还了',
            (TxtCtl.SetColor, 0x2),
            '卢安经济史·上',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    def _loc_FBF(): pass

    label('loc_FBF')

    If(
        (
            (Expr.Eval, "OP_40(0x033E)"),
            Expr.Return,
        ),
        'loc_1017',
    )

    RemoveItem(0x033E, 1)
    OP_28(0x0027, 0x01, 0x0400)
    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '归还了',
            (TxtCtl.SetColor, 0x2),
            '卢安经济史·中',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    def _loc_1017(): pass

    label('loc_1017')

    If(
        (
            (Expr.Eval, "OP_40(0x033F)"),
            Expr.Return,
        ),
        'loc_106F',
    )

    RemoveItem(0x033F, 1)
    OP_28(0x0027, 0x01, 0x0800)
    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '归还了',
            (TxtCtl.SetColor, 0x2),
            '卢安经济史·下',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    def _loc_106F(): pass

    label('loc_106F')

    Jump('loc_1075')

    def _loc_1072(): pass

    label('loc_1072')

    Jump('loc_1075')

    def _loc_1075(): pass

    label('loc_1075')

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0200)"),
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0400)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0800)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1094',
    )

    OP_64(0x03, 0x0001)

    def _loc_1094(): pass

    label('loc_1094')

    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
